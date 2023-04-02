from firebase import firebase

firebase = firebase.FirebaseApplication('https://fitness-ef4f2-default-rtdb.firebaseio.com/', None)

data = {

    'Email' : 'rohith@gmail.com',
    'Password' : 'rohu@12345'

}
#
firebase.post('fitness-ef4f2-default-rtdb/Users', data)

# result = firebase.get('fitness-ef4f2-default-rtdb/Users', '')
# # print(result)
#
# for i in result.keys():
#     print(result[i]['Email'])