echo "Start testing login!"
siege -c 100 -r 100 -b http://127.0.0.1:5000/login
echo "Start testing database!"
siege -c 10 -r 10 -b http://127.0.0.1:5000/
