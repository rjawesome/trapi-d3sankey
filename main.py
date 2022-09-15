import ujson

def main():
  # read input file
  with open("./input.json") as f:
    data = ujson.load(f)['message']['knowledge_graph']
  output = {'nodes': [], 'edges': []}
  nodeIds: dict[str, int] = {}
  
  # assign nodes
  curNodeId = 0
  for node, nodeData in data['nodes'].items():
    output['nodes'].append(
      {
        "id": curNodeId, 
        "name": f"{node} / {nodeData['name']}"
      }
    )
    nodeIds[node] = curNodeId
    curNodeId += 1
  
  # assign edges
  for _, edgeData in data['edges'].items():
    output['edges'].append(
      {
        "source": nodeIds[edgeData["subject"]],
        "target": nodeIds[edgeData["object"]],
        "value": 1
      }
    )

  # output to file
  with open("./output.json", "w") as f:
    ujson.dump(output, f, indent=2)

if __name__ == '__main__':
  main()