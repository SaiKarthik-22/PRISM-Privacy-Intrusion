"""Optional multi-task transformer architecture for PRISM research.

The shared encoder learns contextual representations while separate heads
predict privacy intent and token-level entity labels. This file defines the
architecture; training requires a properly annotated dataset.
"""

import torch
from torch import nn
from transformers import AutoModel


class PRISMTransformer(nn.Module):
    def __init__(self, model_name="distilbert-base-uncased", num_intents=4, num_entities=7):
        super().__init__()
        self.encoder = AutoModel.from_pretrained(model_name)
        hidden = self.encoder.config.hidden_size
        self.dropout = nn.Dropout(0.2)
        self.intent_head = nn.Linear(hidden, num_intents)
        self.entity_head = nn.Linear(hidden, num_entities)
        self.risk_head = nn.Linear(hidden, 4)

    def forward(self, input_ids, attention_mask=None):
        outputs = self.encoder(input_ids=input_ids, attention_mask=attention_mask)
        sequence = self.dropout(outputs.last_hidden_state)
        pooled = sequence[:, 0, :]
        intent_logits = self.intent_head(pooled)
        risk_logits = self.risk_head(pooled)
        entity_logits = self.entity_head(sequence)
        return {
            "intent_logits": intent_logits,
            "risk_logits": risk_logits,
            "entity_logits": entity_logits,
        }
