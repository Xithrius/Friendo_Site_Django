VALID_LOGIN = """
mutation{
  login(data: {username: "test_api_user", password: "test2244"}){
    token
  }
}
"""

INVALID_LOGIN = """
mutation{
  login(data: {username: "invalid_user", password: "invalid_password"}){
    token
  }
}
"""

GET_USERS = """
{
  allUsers{
    username
  }
}
"""
