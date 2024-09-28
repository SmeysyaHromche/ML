# Neural network with solution for Boston dataset

```json
VALID_JSON = {
    "type":"object",
    "properties":
    {
        "data":
        {
            "type":"object",
            "property":
            {
                "path":
                {
                    "type":"string"
                },
                "src":
                {
                    "type":"array",
                    "items":
                    {
                        "type":"string",
                    }
                },
                "trg":
                {
                    "type":"string"
                },
                "test_size":
                {
                    "type":"integer",
                    "minimum":1,
                    "maximum":100
                }
            },
            "required":["path", "src", "trg", "test_size"]
        },
        "nn_config":
        {
            "type":"object",
            "properties":
            {
                "epochs":
                {
                    "type":"integer"
                },
                "batch_size":
                {
                    "type":"integer",
                },
                "act_f":
                {
                    "type":"string",
                    "enum": ["identity", "relu", "sig"]
                },
                "learning_rate":
                {
                    "type":"number",
                    "minimum": 0.0,
                    "maximum":1.0
                },
                "hidden_cnt":
                {
                    "type":"integer"
                },
                "hidden_size":
                {
                    "type":"integer"
                }
            },  
            "required":["epochs", "batch_size", "act_f", "learning_rate", "hidden_size","hidden_cnt"]
        }
    },
    "required":["data","nn_config"]
}
```