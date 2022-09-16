import ujson
import sys

def main():
  # get arguments
  input_file = sys.argv[1]

  # read input file
  with open(input_file) as f:
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

  print(ujson.dumps(output, indent=2))

if __name__ == '__main__':
  main()