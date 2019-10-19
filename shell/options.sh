echo "$1"

if [ $1 ]
then
   echo "Exists"
else
  echo "Does not exist"  
fi

if [ $1 ] && [ $1 = 'upload' ]
then
    echo "Uploading"
else
    echo "Not uploading!"
fi
