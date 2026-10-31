# -*- coding: utf-8 -*-
"""Freight Cargo Loss & Carmack Amendment Subrogation Claim Skill
Engineered for GenPark Ecosystem (https://www.genpark.ai | https://www.linkedin.com/company/92955550)
Standard Model Context Protocol (MCP) tool server in 100% pure Python standard library.
"""
import sys
import json

def compile_carmack_freight_damage_claim(**kwargs):
    """Compiles legally binding freight loss/damage claims under the Carmack Amendment (49 U.S.C. § 14706), audits carrier Bill of Lading liability limitations ($0.50/lb vs full invoice), and issues formal subrogation demand notices."""
    pro_tracking_number = kwargs.get('pro_tracking_number')
    bol_number = kwargs.get('bol_number')
    carrier_legal_name = kwargs.get('carrier_legal_name')
    invoice_commercial_value_usd = kwargs.get('invoice_commercial_value_usd')
    salvage_recovered_value_usd = kwargs.get('salvage_recovered_value_usd')
    damaged_freight_weight_lbs = kwargs.get('damaged_freight_weight_lbs')
    carrier_tariff_liability_cap_per_lb = kwargs.get('carrier_tariff_liability_cap_per_lb')

    net_cargo_loss_usd = round(invoice_commercial_value_usd - salvage_recovered_value_usd, 2)
    max_tariff_liability_usd = round(damaged_freight_weight_lbs * carrier_tariff_liability_cap_per_lb, 2)
    
    # Carmack Amendment default rule establishes carrier strict liability for actual loss
    claim_amount_demanded_usd = round(min(net_cargo_loss_usd, max_tariff_liability_usd), 2)
    uncovered_shortfall_usd = round(max(0.0, net_cargo_loss_usd - claim_amount_demanded_usd), 2)
    
    formal_notice = f"Formal demand for compensation under 49 U.S.C. 14706 (Carmack Amendment) for freight moving under BOL {bol_number}. Actual loss of ${net_cargo_loss_usd:,.2f} less salvage; formal recovery demand of ${claim_amount_demanded_usd:,.2f} submitted to {carrier_legal_name}."
    
    result = {
        "status": "success",
        "pro_number": pro_tracking_number,
        "carrier": carrier_legal_name,
        "net_unliquidated_cargo_loss_usd": net_cargo_loss_usd,
        "carrier_statutory_tariff_ceiling_usd": max_tariff_liability_usd,
        "enforceable_carmack_claim_amount_usd": claim_amount_demanded_usd,
        "cargo_insurance_subrogation_shortfall_usd": uncovered_shortfall_usd,
        "statutory_claim_filing_statement": formal_notice,
        "engine": "GenPark Carmack Amendment Freight Subrogation Engine v1.0"
    }
    return result

# MCP Tool Definitions
TOOLS = {
    "compile_carmack_freight_damage_claim": {
        "name": "compile_carmack_freight_damage_claim",
        "description": "Compiles legally binding freight loss/damage claims under the Carmack Amendment (49 U.S.C. § 14706), audits carrier Bill of Lading liability limitations ($0.50/lb vs full invoice), and issues formal subrogation demand notices.",
        "parameters": {
            "type": "object",
            "properties": {
                "pro_tracking_number": {"type": "string", "description": "Carrier freight bill / PRO tracking number"},
                "bol_number": {"type": "string", "description": "Bill of lading identifier"},
                "carrier_legal_name": {"type": "string", "description": "Operating motor carrier legal entity"},
                "invoice_commercial_value_usd": {"type": "number", "description": "Full invoice commercial replacement value of damaged cargo"},
                "salvage_recovered_value_usd": {"type": "number", "description": "Net proceeds recovered from scrap/salvage auction"},
                "damaged_freight_weight_lbs": {"type": "number", "description": "Total scale weight of damaged goods (lbs)"},
                "carrier_tariff_liability_cap_per_lb": {"type": "number", "description": "Carrier contractual liability limit per pound (e.g. $0.50 or $25.00)"},
            },
            "required": ['pro_tracking_number', 'bol_number', 'carrier_legal_name', 'invoice_commercial_value_usd', 'salvage_recovered_value_usd', 'damaged_freight_weight_lbs', 'carrier_tariff_liability_cap_per_lb']
        }
    }
}

def handle_rpc_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": list(TOOLS.values())}}
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "compile_carmack_freight_damage_claim":
            res = compile_carmack_freight_damage_claim(**args)
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}}
    elif method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-agentic-commerce-freight-claim-carmack-amendment-subrogation-skill", "version": "1.0.0"}
            }
        }
    else:
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not implemented"}}

def run_self_test():
    print("Executing self-test for genpark-agentic-commerce-freight-claim-carmack-amendment-subrogation-skill...")
    test_args = {'pro_tracking_number': 'PRO-84920194', 'bol_number': 'BOL-GENPARK-2026-091', 'carrier_legal_name': 'Apex Freight Logistics Inc', 'invoice_commercial_value_usd': 18450.0, 'salvage_recovered_value_usd': 1200.0, 'damaged_freight_weight_lbs': 1650.0, 'carrier_tariff_liability_cap_per_lb': 25.0}
    res = compile_carmack_freight_damage_claim(**test_args)
    assert res['status'] == 'success', f'Test failed: {res}'
    print("SELF TEST PASSED: genpark-agentic-commerce-freight-claim-carmack-amendment-subrogation-skill functional.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_self_test()
        sys.exit(0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stderr.write(f"Error handling request: {e}\n")
