# Neural network with solution for MNIST dataset

### Configuration
```json
{
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
                    "minItems":1,
                    "items":
                    {
                        "type":"string",
                    }
                },
                "trg":
                {
                    "type":"string"
                }
            },
            "required":["path", "src", "trg"]
        },
        "hpr_prm":
        {
            "type":"object",
            "properties":
            {
                "epochs":
                {
                    "type":"integer",
                    "minimum":10
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
                "hidden_layer":
                {
                    "type":"array",
                    "minItems":2,
                    "maxItems":2,
                    "items":
                    {
                        "type":"integer"
                    }
                }
            },
            "required":["epochs", "act_f", "learning_rate", "hidden_layer"]
        }
    },
    "required":["data","hpr_prm"]
}
```