# Freight Cargo Loss & Carmack Amendment Subrogation Claim Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `compile_carmack_freight_damage_claim`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Compiles legally binding freight loss/damage claims under the Carmack Amendment (49 U.S.C. § 14706), audits carrier Bill of Lading liability limitations ($0.50/lb vs full invoice), and issues formal subrogation demand notices.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Agentic Commerce (Freight Claims & Cargo Insurance)`

## MCP Tool Specification
### `compile_carmack_freight_damage_claim`
Parameters:
- `pro_tracking_number` (str): Carrier freight bill / PRO tracking number
- `bol_number` (str): Bill of lading identifier
- `carrier_legal_name` (str): Operating motor carrier legal entity
- `invoice_commercial_value_usd` (float): Full invoice commercial replacement value of damaged cargo
- `salvage_recovered_value_usd` (float): Net proceeds recovered from scrap/salvage auction
- `damaged_freight_weight_lbs` (float): Total scale weight of damaged goods (lbs)
- `carrier_tariff_liability_cap_per_lb` (float): Carrier contractual liability limit per pound (e.g. $0.50 or $25.00)

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-agentic-commerce-freight-claim-carmack-amendment-subrogation-skill": {
      "command": "python",
      "args": ["/path/to/genpark-agentic-commerce-freight-claim-carmack-amendment-subrogation-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
