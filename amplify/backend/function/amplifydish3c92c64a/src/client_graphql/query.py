from gql import gql

def listProjects():
    query_string = gql("""   
query listProjects {
  listProjects {
    items {
      name
      description
      projectManager{
        name
      }
      developers{
        name
      }
    }
    nextToken
  }
}""")
    return query_string    

def dict_input(item):
    return item