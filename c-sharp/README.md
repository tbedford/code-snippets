# Getting .NET running on the command line

Don't. Instead use Visual Studio Community Edition. You will need a Microsoft Account.

If you really want to.

1. Create a directory for your project.
2. Create a project `.csproj` file such as:

    ``` xml
    <Project Sdk="Microsoft.NET.Sdk">
        <PropertyGroup>
            <OutputType>Exe</OutputType>
            <TargetFramework>net5.0</TargetFramework>
        </PropertyGroup>
        <ItemGroup>
            <PackageReference Include="ably.io" Version="1.2.5" />
        </ItemGroup>
    </Project>
    ```

    This is in your project directory.

3. You'll need the `dotnet` command line tool. I think I downloaded this and installed from Microsoft, not `brew`. Probably should have used `brew`.
4. Make sure you are in the project directory. Run the following command:

``` shell
dotnet build TestAbly.csproj
```

This will cmpile/build your project.
5. Run the code with:

``` shell
dotnet run TestAbly
```

