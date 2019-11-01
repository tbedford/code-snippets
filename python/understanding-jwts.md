# Understanding JWTs

In this article I take a look at JSON Web Tokens (JWTs). JWTS seem to cause a lot of confusion for our customers at Nexmo. I was new to thenm when I starrted at Nexmo. So I decided to write up some notes that will hopefully clarify what they are, what they are used for, and how to create them. I will also present some Python code that creates a JWT and uses it in an API call.

## What is a JWT used for?

A JWT is a special token that can be used in a variety of applications. The use case I look at here is using a JWT to authenticate a REST API call. I will use the Nexmo REST API to demonstrate this.

## What is a JWT?

As the name implies the JWT is essentially a piece of JSON code. It has three main parts:

1. Header
2. Payload
3. Signature

These are joined by the '.' character in this format:

``` shell
xxxxx.yyyyy.zzzzz
```

### Header

The header typically looks like this:

``` json
{
  "alg": "RS256",
  "typ": "JWT"
}
```

The header is also Base64Url encoded to form the first part of the JWT. What exactly is Base64Url encoding? I will cover that in another article as it's quite interesting, but for now you don't need to worry about it as the JWT library we will use does this for you.

The main feature of the header is it specifies the algorithm that is going to be used to sign the JWT. Nexmo requires the JWT to be signed using RS256, so that's what I specified here.

### Payload

The payload contains what are called _claims_. The three types of claims are:

1. Registered - these are predefined.
2. Public - these can be user-defined.
3. Private - these are used to share information between parrties concerned.

The payload is essentially a piece of JSON into which you put certain things. Those things are sometimes mandatory, and sometimes optional. For example, when using JWTs to authenticate a Nexmo API call the `application_id` is a required (public) claim. It also requires the private claims `iat` and `jti` in the payload. Don't worry about those for now, I will get to them shortly.

Once your payload is built it is Base64Url encoded to form the second part of the JWT.

The claims required for Nexmo API calls are as follows:

<table border="1">
<tr><th>Claim</th><th>Description</th><th>Mandatory</th></tr>
<tr><td>`application_id`</td><td>The unique ID allocated to your application by Nexmo.</td><td>Yes</td></tr>
<tr><td>`iat`</td><td>The Unix timestamp at UTC + 0 indicating the moment the JWT was requested.</td><td>Yes</td></tr>
<tr><td>`jti`</td><td>The unique ID of the JWT.</td><td>Yes</td></tr>
<tr><td>`nbf`</td><td>The Unix timestamp at UTC + 0 indicating the moment the JWT became valid. </td><td>No</td></tr>
<tr><td>`exp`</td><td>The Unix timestamp at UTC + 0 indicating the moment the JWT is no longer valid. A minimum value of 30 seconds from the time the JWT is generated. A maximum value of 24 hours from the time the JWT is generated. A default value of 15 minutes from the time the JWT is generated.</td><td>No</td></tr>
</table>

The observant of you will now understand why I looked at Unix timestamps in the [previous article](/articles/unix-time.html)!

In our code we will generate the JWT dynamically each time we make a call, so we are fine with the default expiry time of 15 minutes. So we can ignore the `exp` claim (although I show how to set it in the complete example code). We can also ignore `nbf` item as well - we want our JWT to be valid immediately.

As `iat` is mandatory we will need to create that. It is essentially a Unix timestamp for "now" that can be created in Python using `time.time()`. You see how it's generated later.

The `jti` is a nonce or UUID to uniquely identify the JWT. There are no particular requirements on this as long as the ID is unique. In PAW for example a nonce is created of the form `vvXjP5vxCgRliyo8ApQOyKqcotfQdaB5` - that is, a 32 character string consisting of lowercase letters, uppercase letters and digits. I really should talk about PAW in another article. I've been using it about eight months now and this it's very good. Anyway, I digress. In this article I will generate the `jti` using Python's `uuid4()` function. You know all about UUIDs as I use them a lot on this site.

### Signature

The third part is the trickiest. The signature is basically the first two parts concatenated using '.' and then signed using a secret and the algorithm specified in the header.

In the case of the Nexmo API the secret used is the private key for the application you are invoking API calls against. Authentication in Nexmo is done on a per-application basis. This is also why the application ID is contained in the payload.

For the Nexmo API the JWT algorithm must be RS256.

## Creating a JWT

Without further ado here's the code snippet (I will list the complete code later) for creating a JWT that is suitable for authenticating the Nexmo API.

**NOTE:** You don't normally need to do this if you are using one of the Nexmo client libraries as the library generates the JWTs for you automatically. I am using Nexmo simply as a way to verify that my JWT generation worked correctly.

So, I'm using the standard JWT library imported with `import jwt`. From this you can see it's fairly easy to build the payload:

``` python
application_id = "your_application_id"

payload = {
    'application_id': application_id,
    'iat': int(time.time()),
    'jti': str(uuid4()),
}

# Read in private key from store
filename =  "path/to/private.key"
f = open(filename, 'r')
private_key = f.read()
f.close()

jwt = jwt.encode(payload, private_key, algorithm='RS256')
```

The private key generated for the Nexmo application is used to sign the JWT.

Alos, I have created the payload in the simplest possible way here, but in future I will show you how to write a proper Python method to more flexibly and robustly create the payload.

## Using the JWT

Now that the JWT has been generated, we need to test it out. I do this by making a Nexmo API call that is authenticated via JWT. I used the `requests` library to do this. Instead of Python code you could also have used the JWT in a PAW request, or via a Curl request on the API. Here's the API call snippet:

``` python
auth = b'Bearer '+jwt
headers = {'Authorization': auth, 'Content-Type': 'application/json'}
r = requests.get('https://api.nexmo.com/v1/calls', headers=headers)
print(r)
```

You'll notice the JWT is contained in the header. This particular API call returns all the Nexmo calls I've made. I won't go into the Nexmo response in any detail here as I just needed to verify a 200 response back (200 is the "all good" status code).

## Complete example code

For the sake of completeness (and possible future reference on my part) I list the complete test code here:

``` python
import jwt
import time
import json
import requests
from uuid import uuid4
from pprint import pprint

application_id = "APP_ID"
filename =  "private.key"
expiry = 1*60*60 # JWT expires after one hour (default is 15 minutes)

payload = {
    'application_id': application_id,
    'iat': int(time.time()),
    'jti': str(uuid4()),
    'exp': int(time.time()) + expiry,
}

# Read in private key from store
f = open(filename, 'r')
private_key = f.read()
f.close()

jwt = jwt.encode(payload, private_key, algorithm='RS256')

# Then make a call - retrieve info for all calls https://api.nexmo.com/v1/calls
auth = b'Bearer '+jwt
headers = {'Authorization': auth, 'Content-Type': 'application/json'}
r = requests.get('https://api.nexmo.com/v1/calls', headers=headers)
j = r.json()
calls = j['_embedded']['calls']
for call in calls:
    pprint(call)
```

I used the `Requests` library to make the HTTP call. I really love the simplicity of Requests. That is another library I will need to talk about more in a future article. In this case the JWT is passed in the header of the call. If you were doing this API using Curl it would look like:

``` shell
curl 'https://api.nexmo.com/v1/calls' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOiIxNTQxMDYwMjMwIiwiZXhwIjoxNTQxMDYwMjkwLCJqdGkiOiJZNThTRFJ7aTBvZUVwUm5MSlVFaDNnQ09qS292MVl5bSIsImFwcGxpY2F0aW9uX2lkIjoiOWVhZDIwYTktZjdkOC00YzRmLWExMTEtZTkwMmI1ODUyZmQ0In0.fOFocUiugpE-tzUBSFOQcIYqPiEnK8MBhOTn1QczylIm56ObVcrbLX-7xiHmz5lMXTkHL3Vf12Iq8NGY9RgNxLwBQ63ZwGk_UxKiYt7RfbJajPfram29ofByznGyGeaT960rqCbVu-wOLtQO-rAarpr2w_mAuqQulaQNNrXEq5xG6DD5_LQA_4R1s7haXwvtZt7QOSIiJ2RiCDl1a4qlvc_EkjHHeE7FRIQL1CnbYvnbpIjABCpKzcQCCKNBQT8NtBEDeDzkZ_Uea2GeDSwJ2GR_eSGR394vVIl93WXFZROBmz_UJWBJQ8GC5WQCyuo6EclsbTfpTVFYK2jh7yhBjw' -H 'Content-Type: application/json'
```

If you look carefully at the JWT you will see the `xxx.yyy.zzz` structure. If you look at the documentation for this particualr API you'll see it needs to be JSON application type so that is added to the header too.

## Summary

I hope this article has demystified JWTs a little for you. There's a lot we didn't cover, but hopefully you now have a good starting point.

## Resources

- <https://jwt.io> - a great site for testing out your generated JWTs for validity.
- <https://pyjwt.readthedocs.io/en/latest/usage.html#encoding-decoding-tokens-with-rs256-rsa>
- <http://docs.python-requests.org/en/master/user/advanced/#custom-authentication>
- <http://docs.python-requests.org/en/master/user/quickstart/#custom-headers>
