
users_list = [
    "johndoe123",
    "janesmith456",
    "coderking",
    "techie_gal",
    "python_pro",
    "dev_guru",
    "hacker101",
    "data_cruncher",
    "ai_master",
    "cloud_ninja"
]

class Graph:
    def __init__(self):
        self.___nodes = {}
        pass

    def append(self, data):
        self.___nodes[data] = { "connections": 0,
                             "list": set([])
                            }

    def getNodes(self):
#         Time Complexity: O(n)
#         Auxiliary Space: O(n)
        return self.___nodes.keys()
    
    def making_connection(self, node_name, connection):
        if(connection == node_name):
            print("Not possible to execute")
            return
         
        new_friend = self.___nodes[connection]
        
        if(new_friend == None):
            print("Not possible to execute")
            return
        
        target = self.___nodes[node_name]

        if(connection in target["list"] ):
            return
        

        target["list"].update([connection])
        target["connections"] = target["connections"] + 1

        new_friend["list"].update([node_name])
        new_friend["connections"] = new_friend["connections"] + 1



        self.___nodes[node_name] = target
        self.___nodes[connection] = new_friend

    def get_nodes_and_connections(self):
        for key, value in self.___nodes.items():
            if(value["list"] == set()):
                print(key, ":", "No connections yet")
                continue
            print(key, ":", value)

    def get_a_connections_from(self, node_name):
         node = self.___nodes[node_name]
         if(node == None):
            print("Not possible to execute")
            return
         print("Connections from: ", node_name)
         print("Connections: ", node["connections"])
         for connections in node["list"]:
             print("=> ", connections)

        

user = Graph()

for u in users_list:
    user.append(u)

print(" ")
user.making_connection("hacker101", "ai_master")
user.making_connection("hacker101", "cloud_ninja")
user.get_nodes_and_connections()
print(" ")
user.get_a_connections_from("hacker101")
