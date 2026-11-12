import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = json.loads((ROOT / "registry/functionality-vault-54-batch03.json").read_text())

def test_families():
    assert set(REGISTRY["sourceFamilies"]) == {"zenith", "toonhub", "craftline", "obsidian", "little-lantern"}

def test_contracts():
    records = REGISTRY["capabilities"]
    assert len(records) == 22
    assert len({x["id"] for x in records}) == 22
    assert all(x["status"] == "SPECIFIED" and x["requiresRuntimeVerification"] for x in records)
    assert all(x["inputs"] and x["outputs"] and x["acceptance"] for x in records)

def test_source_constants():
    c = REGISTRY["referenceConstants"]
    assert c["toonhub"]["transitionMs"] == 650
    assert c["craftline"]["crossfadeSeconds"] == 1.4
    assert c["obsidian"]["lruMax"] == 28
    assert c["obsidian"]["watchdogMs"] == 45000
    assert c["little-lantern"]["pageSegments"] == [32, 10]
    assert c["zenith"]["propertyCount"] == 3
    assert len(c["zenith"]["chartData"]) == 3
