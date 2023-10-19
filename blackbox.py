import json

output_data = ""
basic_imports = "from diagrams import Cluster, Diagram, Edge, Node\n"

with open("./input_data.json") as file:
    json_data = json.load(file)
    
    output_data_imports = ""
    for key in json_data["node_dependencies"]:
        module = key.rsplit(".", maxsplit=1)
        output_data_imports += "from " + module[0] + " import " + module[1] + "\n"

    diagram_context = ""
    diagram_context = f"with Diagram('{json_data['graph_display_name']}', show=False):\n"
    connections = []

    for node, detail in json_data["graph_structure"].items():
        if detail["type"] == "node":
            connections.append(node)
            diagram_context += "\t" + node + " = " + detail["info"]["node_type"] + f"('{detail['info']['label']}')" + "\n"
        
        if detail["type"] == "cluster":
            sub_connections = []
            diagram_context += f"\twith Cluster('{detail['label']}'):\n"
            for sub_node in detail["info"] :
                if sub_node["type"] == "node":
                    sub_connections.append(sub_node['id'])
                    diagram_context += "\t\t" + sub_node['id'] + " = " + sub_node["info"]["node_type"] + f"('{sub_node['info']['label']}')" + "\n"
            connections.append(str(sub_connections).replace("'", ""))

output_data += basic_imports + output_data_imports + diagram_context + '\t' + ' >> '.join(connections)

with open("./output_data.py", "w") as file:
    file.write(output_data)

print(output_data)