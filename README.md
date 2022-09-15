# trapi-d3sankey

Input your TRAPI output in ``input.json`` such as
```json
{
   "message":{
      "knowledge_graph":{
         "nodes": {
            "MONDO:0018982":{
               "categories":[
                  "biolink:Disease"
               ],
               "name":"Niemann-Pick disease type C",
               "attributes":[
                  {
                     "attribute_type_id":"biolink:xref",
                     "value":[
                        "MONDO:0018982",
                        "ORPHANET:646",
                        "UMLS:C0220756",
                        "UMLS:C0268247",
                        "MESH:D052556",
                        "NCIT:C85214",
                        "SNOMEDCT:66751000"
                     ]
                  },
                  {
                     "attribute_type_id":"biolink:synonym",
                     "value":[
                        "Niemann-Pick disease type C",
                        "Niemann-Pick Disease, Type C",
                        "Niemann-Pick Disease, Type D"
                     ]
                  }
               ]
            },
            ...
         },
         "edges": {
            "5465a16df9ff590b86888802039331be":{
               "predicate":"biolink:treats",
               "subject":"PUBCHEM.COMPOUND:5997",
               "object":"MONDO:0018982",
               "attributes":[
                  {
                     "attribute_type_id":"biolink:aggregator_knowledge_source",
                     "value":[
                        "infores:biothings-explorer"
                     ],
                     "value_type_id":"biolink:InformationResource"
                  },
                  ...
               ]
            },
        }
     }
  }
}
```

The appropriate output that can be used in d3 sankey will come out in ``ouptut.json`` like such (source = subject & target = object)
```json
{
    "nodes": [
        {
            "node": 0,
            "name": "MONDO:0018982 / Niemann-Pick disease type C"
        },
        ...
    ],
    "links": [
        {
            "source": 1,
            "target": 0,
            "value": 1
        },
        ...
    ]
}
```