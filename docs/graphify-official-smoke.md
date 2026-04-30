# Graphify Official Smoke Test

- Generated at: 2026-04-30T23:25:52Z
- Graph: `/Users/ali/GRAPHIFY-zoroastrianism/graphify-out/graph.json`
- Scope: read-only official Graphify commands; no rebuild, no merge, no OCR.

## Query

- Exit status: `0`

```text
$ .venv/bin/graphify query What\ connects\ Mithra\ to\ khvarnah\? --graph graphify-out/graph.json --budget 1200
NODE “Building a New Vision of the Past in the Sasanian Empire: The Sanctuaries of Kayānsih and the Great Fires of Iran”\* [src=raw/ocr/Canepa_Building_a_New_Vision_of_the_Past.md loc=None community=18]
NODE ASTYAGES, CYRUS AND ZOROASTER: SOLVING A HISTORICAL DILEMMA [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=None community=3]
NODE **THE AURA OF KINGS** [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=None community=1]
NODE Avesta [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=3]
NODE Reconsidering the Concept of Revolutionary Monotheism Beate Pongratz-Leisten Winona Lake, Indiana EisEnbrauns 2011 Offprint frOm [src=raw/ocr/Academia Summary — Reconsidering the Concept of Revolutionary Monotheism Beate Pongratz-Leisten Winona Lake, Indiana EisEnbrauns 2011 Offprint frOm.md loc=None community=3]
NODE Ahura-Mazda [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=None community=2]
NODE Khvarnah / Farr (Divine Glory) [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Apam Napāt [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Mithra (Lord of Covenants) [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Young Avesta: Yasna, Yashts, Videvdad (Yasht 13.89; Yasna 9.14-15; Yasht 17.18-20; Videvdad 19) [src=raw/ocr/Academia Summary — Reconsidering the Concept of Revolutionary Monotheism Beate Pongratz-Leisten Winona Lake, Indiana EisEnbrauns 2011 Offprint frOm.md loc=chunk 1/1 community=3]
NODE Khvarenah [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE ‘Avestan’ Sites of Memory [src=raw/ocr/Canepa_Building_a_New_Vision_of_the_Past.md loc=chunk 3/3 community=18]
NODE Old Avesta: Gathas, Yasna Haptanghaiti, and Airyaman (Yasna 54.1) [src=raw/ocr/Academia Summary — Reconsidering the Concept of Revolutionary Monotheism Beate Pongratz-Leisten Winona Lake, Indiana EisEnbrauns 2011 Offprint frOm.md loc=chunk 1/1 community=3]
NODE Mithraic Initiation Oath, Hierarchy, and Symbols [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Cyrus, Darius, and Achaemenid Ideology [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Avestan Priestly Redaction Thesis [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 3/3 community=3]
NODE Yashts 13:94–95 (Yts 13:94–95) [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 3/3 community=3]
NODE Great Fires of Iran [src=raw/ocr/Canepa_Building_a_New_Vision_of_the_Past.md loc=chunk 3/3 community=18]
NODE Farvardin Yasht 13:94–95 [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 2/3 community=1]
NODE Koranic ʿahd allāh (“Covenant with God”; note 183) [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Kellens’s Darius Genealogy Hypothesis 
... (truncated to ~1200 token budget)
```

## Path

- Exit status: `0`

```text
$ .venv/bin/graphify path Mithra $'Ahura Mazd�\201' --graph graphify-out/graph.json
Shortest path (4 hops):
  Mithraic Solar-Serpent-Lion Iconography (Sasanian Seals and Armenian Mehean Portals) --conceptually_related_to [EXTRACTED]--> Apam Napāt --references [EXTRACTED]--> **THE AURA OF KINGS** --references [EXTRACTED]--> Ahura Mazdā --conceptually_related_to [EXTRACTED]--> Yasna Haptaṅhāiti Fire Ritual and Ahura Mazdā's Presence (Y. 34.4; Y. 36.2–6)
```

## Explain

- Exit status: `0`

```text
$ .venv/bin/graphify explain Zarathustra --graph graphify-out/graph.json
Node: Zarathustra
  ID:        llm_zarathustra
  Source:    raw/ocr/2008_2009_Avestan_Literature_In_Ronald_E.md chunk 1/3
  Type:      document
  Community: 1
  Degree:    25

Connections (25):
  --> A History of Persian Literature Volume XVII [references] [EXTRACTED]
  --> IRANO-JUDAICA VII [references] [EXTRACTED]
  --> --- Abraham and Nimrod in the Shadow of Zarathustra\* [references] [EXTRACTED]
  --> Gifts to a Magus [references] [EXTRACTED]
  --> Ahura Mazdā [conceptually_related_to] [EXTRACTED]
  --> Reconsidering the Concept of Revolutionary Monotheism Beate Pongratz-Leisten Winona Lake, Indiana EisEnbrauns 2011 Offprint frOm [references] [EXTRACTED]
  --> Zoroastrian Eschatology [conceptually_related_to] [EXTRACTED]
  --> Zarathustra’s Prophetic and Priestly Authority [conceptually_related_to] [EXTRACTED]
  --> Abraham [contrasts_with] [EXTRACTED]
  --> Young Avesta: Yasna, Yashts, Videvdad (Yasht 13.89; Yasna 9.14-15; Yasht 17.18-20; Videvdad 19) [references] [EXTRACTED]
  --> Claim: Israelites Assimilated Zarathustrian Eschatology [conceptually_related_to] [EXTRACTED]
  --> Dual Prophetic-Priestly Authority of Zarathustra [participates_in] [EXTRACTED]
  --> Haug's Zarathustra-Authored Gathas and Reform Thesis [conceptually_related_to] [EXTRACTED]
  --> Zoroastrianism / Mazdayasnian Religion (daēnā mazdayasni; MK fol. 19v.1–4) [conceptually_related_to] [EXTRACTED]
  --> Nimrod [semantically_similar_to] [EXTRACTED]
  --> Old Avesta: Gathas, Yasna Haptanghaiti, and Airyaman (Yasna 54.1) [conceptually_related_to] [EXTRACTED]
  --> The Gathas [conceptually_related_to] [INFERRED]
  --> Authorship, Date, Homeland, and Interpretation Questions around the Gathas [rationale_for] [EXTRACTED]
  --> Vohu Manah-mediated ham-pursagīh Revelation (Y. 43.7–8; Dāityā Tradition) [conceptually_related_to] [EXTRACTED]
  --> Yt. 19.80–81: Demons Retreat Before Zarathustra’s Ahuna Vairya [references] [EXTRACTED]
  ... and 5 more
```

## Benchmark

- Exit status: `0`

```text
$ .venv/bin/graphify benchmark graphify-out/graph.json

graphify token reduction benchmark
──────────────────────────────────────────────────
  Corpus:          627,125 words → ~836,166 tokens (naive)
  Graph:           996 nodes, 2,449 edges
  Avg query cost:  ~7,632 tokens
  Reduction:       109.6x fewer tokens per query

  Per question:
    [92.3x] how does authentication work
    [108.0x] what is the main entry point
    [121.8x] how are errors handled
    [92.9x] what connects the data layer to the api
    [152.5x] what are the core abstractions
```

## Hook Status

- Exit status: `0`

```text
$ .venv/bin/graphify hook status
post-commit: installed
post-checkout: installed
```

