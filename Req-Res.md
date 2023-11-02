# Endpoints

## POST ENDPOINT
```
http://192.168.138.156:5001/api/save_data
```
```
{
    "user_id": 1,
    "name": "Pavan",
    "age": 25,
    "city": "Hyd"
}
```
```
curl --location 'http://192.168.138.156:5001/api/save_data' \
--header 'Content-Type: application/json' \
--data '{
    "user_id": 1,
    "name": "Pavan",
    "age": 25,
    "city": "Hyd"
}
'
```
## GET ENDPOINT (Get get all the users details)
```
http://192.168.138.156:5001/api/get_data
```
```
curl --location 'http://192.168.138.156:5001/api/get_data'
```
## GET ENDPOINT (Get a specific user details)
```
http://192.168.138.156:5001/api/get_user/1
```
```
curl --location 'http://192.168.138.156:5001/api/get_user/1'
```

## PUT ENDPOINT ( Update user data )
```
http://192.168.138.156:5001/api/modify_user/1
```
```
{
    "user_id": 1,
    "name": "Pavan Kumar",
    "age": 25,
    "city": "Hyd"
}
```
```
curl --location --request PUT 'http://192.168.138.156:5001/api/modify_user/1' \
--header 'Content-Type: application/json' \
--data '{
    "user_id": 1,
    "name": "Pavan Kumar",
    "age": 25,
    "city": "Hyd"
}
'
```


## DELETE USER (Delete user by user_id)
```
http://192.168.138.156:5001/api/delete_user/1
```
```
curl --location --request DELETE 'http://192.168.138.156:5001/api/delete_user/1'
```
