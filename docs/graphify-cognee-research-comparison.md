# Graphify vs Cognee Research Query Comparison

- Generated at: `2026-04-30T22:48:30Z`
- Graphify graph: `/Users/ali/GRAPHIFY-zoroastrianism/graphify-out/graph.json`
- Cognee dataset: `zoroastrianism_corpus`
- Source corpus: `/Users/ali/GRAPHIFY-zoroastrianism/graphify-input/ocr-markdown-clean`
- Scope: read-only comparison queries; no graph rebuild, no graph merge, no OCR.

## Summary

- Result: 16/16 commands succeeded.
- Graphify behavior: fast local graph traversal, source-heavy node/edge output, best for seeing relationships, paths, provenance, and community structure.
- Cognee behavior: slower synthesized answers, best for readable prose answers, but the current CLI output includes verbose Cognee logs and does not cite sources as cleanly as Graphify.
- Runtime comparison: Graphify averaged about 0.7s per query; Cognee averaged about 28.8s per query.
- Practical use: use Graphify first to inspect structure and source paths, then Cognee when you want a natural-language synthesis from the ingested memory.

## Mithra / Mithras

Question: What does the corpus say about Mithra or Mithras, especially covenant, initiation, solar symbolism, and social role?

### Graphify

- Exit status: `0`
- Runtime: `0.8s`
- Command: `graphify query 'What does the corpus say about Mithra or Mithras, especially covenant, initiation, solar symbolism, and social role?' --graph graphify-out/graph.json --budget 1600`

```text
NODE Dialogue Between Cultures & Exchange of Knowledge And Cultural Ideas [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=None community=7]
NODE **THE AURA OF KINGS** [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=None community=1]
NODE Gifts to a Magus [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=None community=1]
NODE Ahura Mazdā [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Zarathustra [src=raw/ocr/2008_2009_Avestan_Literature_In_Ronald_E.md loc=chunk 1/3 community=1]
NODE Avesta [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=3]
NODE Ahura-Mazda [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=None community=2]
NODE 02239118 [src=raw/ocr/02239118.md loc=None community=25]
NODE Khvarnah / Farr (Divine Glory) [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Cultural Remnants of Ancient Iran in Turkish Classical Works of the XI-XII Centuries [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Women Priests and Charismatic Gender-Inclusive Authority [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 3/3 community=1]
NODE Zarathustra’s Prophetic and Priestly Authority [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Claim: Indo-Iran bilateral relations are ancient, continuous, and worth preserving [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 3/3 community=7]
NODE Sasanian Dynasty [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Apam Napāt [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Indo-Iranian cultural and knowledge exchange [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Argument: Ancient Iranian Culture Shaped XI-XII c. Turkish Classical Works after Islam [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Mithra (Lord of Covenants) [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Article Argument: Zarathustra’s Prophetic and Priestly Authority (Max Weber Typology) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 2/3 community=1]
NODE Account of a Bas-relief of Mithras Found at York [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Dual Prophetic-Priestly Authority of Zarathustra [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 3/3 community=1]
NODE Khvarenah [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE York/Micklegate Bas-relief of Mithras (dug up 1747) [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Mithraic Initiation Oath, Hierarchy, and Symbols [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Cyrus, Darius, and Achaemenid Ideology [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Argument: Persia/Iran as intermediary for East–West cultural transmission [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Minoye Kherad / Minouch of Wisdom [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Mithriac Ceremonies and Mysteries [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Zoroastrianism / Mazdayasnian Religion (daēnā mazdayasni; MK fol. 19v.1–4) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Abolfazl Khatibi's Shahnameh-Minoye Kherad Comparison [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Y. 45.3: Divine maqθrəm Revelation to the Poet-Priest [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 2/3 community=1]
NODE Yt. 19.80–81: Demons Retreat Before Zarathustra’s Ahuna Vairya [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 2/3 community=1]
NODE Shared Indo-Persian Aryan origin and migration from Central Asia or northern region [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 3/3 c
... (truncated to ~1600 token budget)
```

### Cognee

- Exit status: `0`
- Runtime: `33.5s`
- Command: `.venv/bin/cognee-zoro query 'What does the corpus say about Mithra or Mithras, especially covenant, initiation, solar symbolism, and social role?'`

```text
2026-04-30T22:48:32.192063 [info     ] Deleted old log file: /Users/ali/.cognee/logs/2026-04-30_14-11-19.log [cognee.shared.logging_utils]

2026-04-30T22:48:32.192526 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-48-31.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-48-31.log

2026-04-30T22:48:32.192801 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:48:32.193028 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:48:32.193259 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:48:41.285519 [info     ] Loaded JSON extension          [cognee.shared.logging_utils]

2026-04-30T22:48:42.023390 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-48-31.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-48-31.log

2026-04-30T22:48:42.023828 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:48:42.024125 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:48:42.024387 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:48:48.383198 [info     ] Vector collection retrieval completed: Retrieved distances from 6 collections in 0.50s [cognee.shared.logging_utils]

2026-04-30T22:48:48.384442 [info     ] Retrieving ID-filtered graph from database. [CogneeGraph]

2026-04-30T22:48:49.262949 [info     ] ID-filtered retrieval: 2690 nodes and 4493 edges in 0.88s [cognee.shared.logging_utils]

2026-04-30T22:48:50.108081 [info     ] Graph projection completed: 2690 nodes, 4493 edges in 0.84s [CogneeGraph]

2026-04-30T22:48:50.181479 [info     ] Completed resolving edges to text [cognee.shared.logging_utils] extra={'node_count': 11, 'connection_count': 10}
The corpus describes Mithra as an ancient god associated with covenants, light, and contracts, particularly emphasized in Mithraic societies, which functioned as brotherhoods requiring initiation rites and oaths administered under Mithra's authority as the Lord of covenants. The god's role included solar symbolism, depicted through motifs like the solar disk and the connection to superior powers such as Ahura Mazda, fostering legitimacy and divine sanction in rulers. Initiation into Mithraic societies often bore implications for social roles, wherein membership allowed for continued adherence to other faiths, with the rites and symbols serving dual purposes in the ritualistic and political contexts.
```

## Khvarnah / Farr

Question: What does the corpus say about khvarnah, farr, royal glory, and kingly legitimacy?

### Graphify

- Exit status: `0`
- Runtime: `0.8s`
- Command: `graphify query 'What does the corpus say about khvarnah, farr, royal glory, and kingly legitimacy?' --graph graphify-out/graph.json --budget 1600`

```text
NODE Dialogue Between Cultures & Exchange of Knowledge And Cultural Ideas [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=None community=7]
NODE BETWEEN THE SAFAVIDS AND THE MUGHALS: ART AND ARTISTS IN TRANSITION\* [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=None community=23]
NODE Gifts to a Magus [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=None community=1]
NODE Ahura Mazdā [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Zarathustra [src=raw/ocr/2008_2009_Avestan_Literature_In_Ronald_E.md loc=chunk 1/3 community=1]
NODE Farrukh Beyg [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 1/3 community=23]
NODE Three Safavid-Mughal Migratory Waves (1544-1585) [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 1/3 community=23]
NODE Zarathustra’s Prophetic and Priestly Authority [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Cultural Remnants of Ancient Iran in Turkish Classical Works of the XI-XII Centuries [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Women Priests and Charismatic Gender-Inclusive Authority [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 3/3 community=1]
NODE Claim: Indo-Iran bilateral relations are ancient, continuous, and worth preserving [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 3/3 community=7]
NODE Indo-Iranian cultural and knowledge exchange [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Between the Safavids and the Mughals: Art and Artists in Transition [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 1/3 community=23]
NODE Sasanian Dynasty [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Argument: Ancient Iranian Culture Shaped XI-XII c. Turkish Classical Works after Islam [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Article Argument: Zarathustra’s Prophetic and Priestly Authority (Max Weber Typology) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 2/3 community=1]
NODE Topkapı Haft awrang (TKS H.1483, copied by Muḥibb ʿAlī, 1570–72) [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 2/3 community=23]
NODE Dual Prophetic-Priestly Authority of Zarathustra [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 3/3 community=1]
NODE Haft awrang Painting Attribution and Dating [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 3/3 community=23]
NODE Mughal Library-Atelier and School of Painting [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 1/3 community=23]
NODE Argument: Persia/Iran as intermediary for East–West cultural transmission [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Zoroastrianism / Mazdayasnian Religion (daēnā mazdayasni; MK fol. 19v.1–4) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Minoye Kherad / Minouch of Wisdom [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Abolfazl Khatibi's Shahnameh-Minoye Kherad Comparison [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Third-Wave Patronage Migration Argument: loss of Safavid patronage and Mughal demand [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 2/3 community=23]
NODE Farrukh Beyg's departure to India and Mughal-court arrival, c. 1585 [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 3/3 community=23]
NODE Muḥammadī [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 2/3 community=23]
NODE Kutadgu Bilig (Knowledge of Happiness) [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Y. 45.3: Divine maqθrəm Revelation to the Poet-Priest [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 2/3 community=1]
NODE 1468 Gulistān of Sa'dī (FGA, F1998.5) as Jousting Field [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 1/3 community=23]
NODE Yt. 19.80–81: Demons Retreat Before Zarathustra’s Ahuna Vairya [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 2/3 community=1]
NODE Chaturanga–Shatranj chess transmission from India to Persia [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Shared Indo-Persian Aryan origin and migration from Central Asia or northern region [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 3/3 community=7]
NODE Ritual Fire as Ahura Mazdā’s Presence and frašō.kərəti Anticipation (Y. 36.2–6) [src=
... (truncated to ~1600 token budget)
```

### Cognee

- Exit status: `0`
- Runtime: `30.8s`
- Command: `.venv/bin/cognee-zoro query 'What does the corpus say about khvarnah, farr, royal glory, and kingly legitimacy?'`

```text
2026-04-30T22:49:06.596058 [info     ] Deleted old log file: /Users/ali/.cognee/logs/2026-04-30_14-11-47.log [cognee.shared.logging_utils]

2026-04-30T22:49:06.596713 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-49-06.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-49-06.log

2026-04-30T22:49:06.597005 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:49:06.597242 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:49:06.597481 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:49:15.339075 [info     ] Loaded JSON extension          [cognee.shared.logging_utils]

2026-04-30T22:49:15.856370 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-49-06.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-49-06.log

2026-04-30T22:49:15.856837 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:49:15.857254 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:49:15.857587 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:49:21.388693 [info     ] Vector collection retrieval completed: Retrieved distances from 6 collections in 0.38s [cognee.shared.logging_utils]

2026-04-30T22:49:21.390154 [info     ] Retrieving ID-filtered graph from database. [CogneeGraph]

2026-04-30T22:49:22.299657 [info     ] ID-filtered retrieval: 2588 nodes and 4291 edges in 0.91s [cognee.shared.logging_utils]

2026-04-30T22:49:22.889547 [info     ] Graph projection completed: 2588 nodes, 4291 edges in 0.59s [CogneeGraph]

2026-04-30T22:49:22.965163 [info     ] Completed resolving edges to text [cognee.shared.logging_utils] extra={'node_count': 15, 'connection_count': 10}
The corpus highlights *khvarnah* as a symbol of divine glory and kingship in Zoroastrianism, representing authority, legitimacy, and military success. It emphasizes the fluctuating nature of *khvarnah*, which can be gained or lost based on one's deeds. The concept plays a central role in Achaemenid kingly ideology, connecting divine sanction to the ruler's legitimacy. *Farr*, closely linked to *khvarnah*, also underscores royal glory and is portrayed in various iconographic forms.

Overall, the interplay between *khvarnah*, *farr*, and royal imagery illustrates the Iranian perception of kingly legitimacy rooted in divine favor and the constant pursuit of authority.
```

## Ahura Mazda

Question: What does the corpus say about Ahura Mazda, creation, monotheism, and divine authority?

### Graphify

- Exit status: `0`
- Runtime: `1.0s`
- Command: `graphify query 'What does the corpus say about Ahura Mazda, creation, monotheism, and divine authority?' --graph graphify-out/graph.json --budget 1600`

```text
NODE ANCIENT IRANIAN MOTIFS AND ZOROASTRIAN ICONOGRAPHY [src=raw/ocr/Ancient_Iranian_Motifs_and_Zoroastrian_I.md loc=None community=10]
NODE ASTYAGES, CYRUS AND ZOROASTER: SOLVING A HISTORICAL DILEMMA [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=None community=3]
NODE **THE AURA OF KINGS** [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=None community=1]
NODE MORE THAN MEN, LESS THAN GODS [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=None community=17]
NODE --- Monotheism the Zoroastrian Way [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=None community=22]
NODE Gifts to a Magus [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=None community=1]
NODE Ahura Mazdā [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Zarathustra [src=raw/ocr/2008_2009_Avestan_Literature_In_Ronald_E.md loc=chunk 1/3 community=1]
NODE By the Favor of Auramazdā: Kingship and the Divine in the Early Achaemenid Period [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Ahura Mazdā / Ohrmazd [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=chunk 1/3 community=22]
NODE Khvarnah / Farr (Divine Glory) [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Khvarnah / Farr (Iranian Royal Glory) [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 3/3 community=1]
NODE Zoroastrianism [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=chunk 1/3 community=22]
NODE Darius I [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 1/3 community=17]
NODE Zarathustra’s Prophetic and Priestly Authority [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Women Priests and Charismatic Gender-Inclusive Authority [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 3/3 community=1]
NODE Angra Mainyu / Ahreman [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=chunk 1/3 community=22]
NODE Darius I's Imperial Program in Texts and Images [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Apam Napāt [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Farr / Khvarnah (Divine Glory) [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Article Argument: Zarathustra’s Prophetic and Priestly Authority (Max Weber Typology) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 2/3 community=1]
NODE Dual Prophetic-Priestly Authority of Zarathustra [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 3/3 community=1]
NODE Material Creation (gētīy; Ahura Mazdā’s world) [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=chunk 2/3 community=22]
NODE Winged Symbol / Figure in the Winged Ring [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 2/3 community=17]
NODE Achaemenid Winged-Disk Symbolism Debate [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Early Achaemenid Kingship and the Divine [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Winged Figure / Farvahar-Fravashi Symbol [src=raw/ocr/Ancient_Iranian_Motifs_and_Zoroastrian_I.md loc=chunk 1/3 community=10]
NODE Spənta Mainiiu and Amesha Spentas (Life-Giving Immortals) [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=chunk 1/3 community=22]
NODE Avestan Creation/Worship Passages (Vd 1; Y 9.8; Y 37.1–2; Y 58.4–5; Yt 1.1; Y 57.17; Y 30.4; Yt 19.18; Yt 5.1) [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=chunk 2/3 community=22]
NODE Persepolitan Glyptic [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 3/3 community=17]
NODE Lotus-Sunflower Dual Khvarnah Symbolism [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 2/3 community=1]
NODE Zoroastrianism / Mazdayasnian Religion (daēnā mazdayasni; MK fol. 19v.1–4) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Material World as Pro-Cosmic Good Creation [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=chunk 3/3 community=22]
NODE The Aura of Kings [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 3/3 community=1]
NODE Argument: Mithrā and Apam-Napāt Embodied Median Kingly Power [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 2/3 community=1]
NODE The Aura of Kings: Legitimacy and Divine Sanction in Iranian Kingship [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE PFS 389* Old Persian Inscript
... (truncated to ~1600 token budget)
```

### Cognee

- Exit status: `0`
- Runtime: `25.9s`
- Command: `.venv/bin/cognee-zoro query 'What does the corpus say about Ahura Mazda, creation, monotheism, and divine authority?'`

```text
2026-04-30T22:49:38.434597 [info     ] Deleted old log file: /Users/ali/.cognee/logs/2026-04-30_14-14-23.log [cognee.shared.logging_utils]

2026-04-30T22:49:38.435044 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-49-38.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-49-38.log

2026-04-30T22:49:38.435291 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:49:38.435534 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:49:38.435788 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:49:46.670214 [info     ] Loaded JSON extension          [cognee.shared.logging_utils]

2026-04-30T22:49:47.149756 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-49-38.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-49-38.log

2026-04-30T22:49:47.150281 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:49:47.150625 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:49:47.151222 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:49:52.141013 [info     ] Vector collection retrieval completed: Retrieved distances from 6 collections in 0.32s [cognee.shared.logging_utils]

2026-04-30T22:49:52.142162 [info     ] Retrieving ID-filtered graph from database. [CogneeGraph]

2026-04-30T22:49:52.969385 [info     ] ID-filtered retrieval: 2678 nodes and 4362 edges in 0.83s [cognee.shared.logging_utils]

2026-04-30T22:49:53.623596 [info     ] Graph projection completed: 2678 nodes, 4362 edges in 0.65s [CogneeGraph]

2026-04-30T22:49:53.696932 [info     ] Completed resolving edges to text [cognee.shared.logging_utils] extra={'node_count': 17, 'connection_count': 10}
The corpus signifies Ahura Mazda as the principal deity in Zoroastrianism, embodying monotheistic principles and divine authority. It discusses concepts of creation intertwined with Ahura Mazda's role, highlighting His association with the winged-disk symbolism. The deity is pivotal in legitimizing rulership, where the 'aura of kings' reflects divine sanction, intertwining kingly legitimacy with the worship of Ahura Mazda. The relationship between Ahura Mazda and khvarnah further emphasizes the notion of divine glory and authority that affects both creation and governance in ancient Iranian contexts.
```

## Zarathustra Authority

Question: What does the corpus say about Zarathustra's prophetic and priestly authority?

### Graphify

- Exit status: `0`
- Runtime: `0.6s`
- Command: `graphify query 'What does the corpus say about Zarathustra'"'"'s prophetic and priestly authority?' --graph graphify-out/graph.json --budget 1600`

```text
NODE ASTYAGES, CYRUS AND ZOROASTER: SOLVING A HISTORICAL DILEMMA [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=None community=3]
NODE ANCIENT IRANIAN MOTIFS AND ZOROASTRIAN ICONOGRAPHY [src=raw/ocr/Ancient_Iranian_Motifs_and_Zoroastrian_I.md loc=None community=10]
NODE A History of Persian Literature Volume XVII [src=raw/ocr/2008_2009_Avestan_Literature_In_Ronald_E.md loc=None community=8]
NODE IRANO-JUDAICA VII [src=raw/ocr/2019_Defeating_Death_Eschatology_in_Zoro.md loc=None community=19]
NODE **THE AURA OF KINGS** [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=None community=1]
NODE --- Abraham and Nimrod in the Shadow of Zarathustra\* [src=raw/ocr/Abraham_and_Nimrod_in_the_Shadow_of_Zar.md loc=None community=20]
NODE Gifts to a Magus [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=None community=1]
NODE Ahura Mazdā [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Zarathustra [src=raw/ocr/2008_2009_Avestan_Literature_In_Ronald_E.md loc=chunk 1/3 community=1]
NODE Reconsidering the Concept of Revolutionary Monotheism Beate Pongratz-Leisten Winona Lake, Indiana EisEnbrauns 2011 Offprint frOm [src=raw/ocr/Academia Summary — Reconsidering the Concept of Revolutionary Monotheism Beate Pongratz-Leisten Winona Lake, Indiana EisEnbrauns 2011 Offprint frOm.md loc=None community=3]
NODE Zoroastrian Eschatology [src=raw/ocr/2019_Defeating_Death_Eschatology_in_Zoro.md loc=chunk 1/3 community=19]
NODE Darius I [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 1/3 community=17]
NODE Zarathustra’s Prophetic and Priestly Authority [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Women Priests and Charismatic Gender-Inclusive Authority [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 3/3 community=1]
NODE Article Argument: Zarathustra’s Prophetic and Priestly Authority (Max Weber Typology) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 2/3 community=1]
NODE Abraham [src=raw/ocr/Abraham_and_Nimrod_in_the_Shadow_of_Zar.md loc=chunk 1/3 community=20]
NODE Young Avesta: Yasna, Yashts, Videvdad (Yasht 13.89; Yasna 9.14-15; Yasht 17.18-20; Videvdad 19) [src=raw/ocr/Academia Summary — Reconsidering the Concept of Revolutionary Monotheism Beate Pongratz-Leisten Winona Lake, Indiana EisEnbrauns 2011 Offprint frOm.md loc=chunk 1/1 community=3]
NODE Haug's Zarathustra-Authored Gathas and Reform Thesis [src=raw/ocr/Academia Summary — Reconsidering the Concept of Revolutionary Monotheism Beate Pongratz-Leisten Winona Lake, Indiana EisEnbrauns 2011 Offprint frOm.md loc=chunk 1/1 community=3]
NODE Winged Figure / Farvahar-Fravashi Symbol [src=raw/ocr/Ancient_Iranian_Motifs_and_Zoroastrian_I.md loc=chunk 1/3 community=10]
NODE Claim: Israelites Assimilated Zarathustrian Eschatology [src=raw/ocr/2019_Defeating_Death_Eschatology_in_Zoro.md loc=chunk 3/3 community=19]
NODE Dual Prophetic-Priestly Authority of Zarathustra [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 3/3 community=1]
NODE Achaemenid Winged-Disk Symbolism Debate [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Khvarenah / xvarənah [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 3/3 community=3]
NODE Old Avesta: Gathas, Yasna Haptanghaiti, and Airyaman (Yasna 54.1) [src=raw/ocr/Academia Summary — Reconsidering the Concept of Revolutionary Monotheism Beate Pongratz-Leisten Winona Lake, Indiana EisEnbrauns 2011 Offprint frOm.md loc=chunk 1/1 community=3]
NODE Nimrod [src=raw/ocr/Abraham_and_Nimrod_in_the_Shadow_of_Zar.md loc=chunk 1/3 community=20]
NODE Argument: Dual Legitimacy Symbolism [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 3/3 community=1]
NODE Zoroastrianism / Mazdayasnian Religion (daēnā mazdayasni; MK fol. 19v.1–4) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Vohu Manah-mediated ham-pursagīh Revelation (Y. 43.7–8; Dāityā Tradition) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Darius and Xerxes Canopied Throne Relief at Persepolis [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 3/3 community=1]
NODE Ritual Fire as Ahura Mazdā’s Presence and frašō.kərəti Anticipation (Y. 36.2–6) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 2/3 community=1]
NODE On the Prophetic and Priestly Authority of Zarathustra [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Yt. 19.80–81: Demons Retreat Before Zarathustra’s Ahuna Vairya [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 2/3 community=1]
NODE Achaemenid Royal Ideology (Darius I,
... (truncated to ~1600 token budget)
```

### Cognee

- Exit status: `0`
- Runtime: `25.8s`
- Command: `.venv/bin/cognee-zoro query 'What does the corpus say about Zarathustra'"'"'s prophetic and priestly authority?'`

```text
2026-04-30T22:50:04.603919 [info     ] Deleted old log file: /Users/ali/.cognee/logs/2026-04-30_14-14-43.log [cognee.shared.logging_utils]

2026-04-30T22:50:04.604303 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-50-04.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-50-04.log

2026-04-30T22:50:04.604531 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:50:04.604751 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:50:04.604981 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:50:11.939008 [info     ] Loaded JSON extension          [cognee.shared.logging_utils]

2026-04-30T22:50:12.430414 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-50-04.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-50-04.log

2026-04-30T22:50:12.430828 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:50:12.431136 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:50:12.431379 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:50:17.103369 [info     ] Vector collection retrieval completed: Retrieved distances from 6 collections in 0.31s [cognee.shared.logging_utils]

2026-04-30T22:50:17.104486 [info     ] Retrieving ID-filtered graph from database. [CogneeGraph]

2026-04-30T22:50:17.910888 [info     ] ID-filtered retrieval: 2620 nodes and 4473 edges in 0.81s [cognee.shared.logging_utils]

2026-04-30T22:50:18.515835 [info     ] Graph projection completed: 2620 nodes, 4473 edges in 0.60s [CogneeGraph]

2026-04-30T22:50:18.589058 [info     ] Completed resolving edges to text [cognee.shared.logging_utils] extra={'node_count': 11, 'connection_count': 10}
The corpus illustrates Zarathustra's prophetic and priestly authority within Zoroastrianism as both foundational and transformative. He is depicted as a major religious reformer who rejected older polytheistic practices and established a focused worship of Ahura Mazda. In the texts, he is often represented as the first human to recite significant prayers like the Ahuna Vairya, reinforcing his role as a priestly figure. His encounters with divine beings and the frameworks of law presented in later texts (like the Videvdad) indicate that he held a significant interpretive authority over religious practice and ethics, shaping the rituals and beliefs that characterize Zoroastrianism.
```

## Jewish Eschatology

Question: What connections does the corpus draw between Zoroastrianism and Jewish eschatology or Second Temple traditions?

### Graphify

- Exit status: `0`
- Runtime: `0.5s`
- Command: `graphify query 'What connections does the corpus draw between Zoroastrianism and Jewish eschatology or Second Temple traditions?' --graph graphify-out/graph.json --budget 1600`

```text
NODE Encounters by the Rivers of Babylon [src=raw/ocr/Abar_Rodestan_i_Babel_The_Zoroastrian_Tr.md loc=None community=5]
NODE IRANO-JUDAICA VII [src=raw/ocr/2019_Defeating_Death_Eschatology_in_Zoro.md loc=None community=19]
NODE --- Abraham and Nimrod in the Shadow of Zarathustra\* [src=raw/ocr/Abraham_and_Nimrod_in_the_Shadow_of_Zar.md loc=None community=20]
NODE BETWEEN THE SAFAVIDS AND THE MUGHALS: ART AND ARTISTS IN TRANSITION\* [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=None community=23]
NODE Zarathustra [src=raw/ocr/2008_2009_Avestan_Literature_In_Ronald_E.md loc=chunk 1/3 community=1]
NODE Farrukh Beyg [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 1/3 community=23]
NODE Zoroastrian Eschatology [src=raw/ocr/2019_Defeating_Death_Eschatology_in_Zoro.md loc=chunk 1/3 community=19]
NODE Three Safavid-Mughal Migratory Waves (1544-1585) [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 1/3 community=23]
NODE Genesis Rabbah 38:11 Abraham and Nimrod Furnace Account [src=raw/ocr/Abraham_and_Nimrod_in_the_Shadow_of_Zar.md loc=chunk 2/3 community=20]
NODE Zarathustra / Zoroaster [src=raw/ocr/Abraham_and_Nimrod_in_the_Shadow_of_Zar.md loc=chunk 2/3 community=20]
NODE Between the Safavids and the Mughals: Art and Artists in Transition [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 1/3 community=23]
NODE Zoroastrian Cosmology as Integral Eschatology [src=raw/ocr/2019_Defeating_Death_Eschatology_in_Zoro.md loc=chunk 2/3 community=19]
NODE Abraham in the Fiery Furnace Narrative [src=raw/ocr/Abraham_and_Nimrod_in_the_Shadow_of_Zar.md loc=chunk 1/3 community=20]
NODE Topkapı Haft awrang (TKS H.1483, copied by Muḥibb ʿAlī, 1570–72) [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 2/3 community=23]
NODE Zoroastrian Influence Debate / Cross-Fertilization Claim (Panaino 2004b; Silverman 2012; Shaked 1984) [src=raw/ocr/2019_Defeating_Death_Eschatology_in_Zoro.md loc=chunk 1/3 community=19]
NODE dēn as Authoritative Oral/Sacred Priestly Tradition [src=raw/ocr/Abar_Rodestan_i_Babel_The_Zoroastrian_Tr.md loc=chunk 2/3 community=5]
NODE Jewish Eschatology [src=raw/ocr/2019_Defeating_Death_Eschatology_in_Zoro.md loc=chunk 3/3 community=19]
NODE Abraham [src=raw/ocr/Abraham_and_Nimrod_in_the_Shadow_of_Zar.md loc=chunk 1/3 community=20]
NODE Avesta: Zoroastrian Sacred Corpus [src=raw/ocr/Abar_Rodestan_i_Babel_The_Zoroastrian_Tr.md loc=chunk 1/3 community=5]
NODE Abar Rōdestān ī Babēl: The Zoroastrian Tradition – the dēn – in Sasanian and Early Islamic Times [src=raw/ocr/Abar_Rodestan_i_Babel_The_Zoroastrian_Tr.md loc=chunk 1/3 community=5]
NODE Zand ī fragard ī jud-dēw-dād (TD2, pp. 453–455, 481–483) [src=raw/ocr/Abar_Rodestan_i_Babel_The_Zoroastrian_Tr.md loc=chunk 3/3 community=5]
NODE Final Resurrection, Universal Judgement, and Molten-Metal Purification [src=raw/ocr/2019_Defeating_Death_Eschatology_in_Zoro.md loc=chunk 2/3 community=19]
NODE Haft awrang Painting Attribution and Dating [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 3/3 community=23]
NODE Claim: Israelites Assimilated Zarathustrian Eschatology [src=raw/ocr/2019_Defeating_Death_Eschatology_in_Zoro.md loc=chunk 3/3 community=19]
NODE Rationale: Midrashic Reversal of Zarathustra Traditions [src=raw/ocr/Abraham_and_Nimrod_in_the_Shadow_of_Zar.md loc=chunk 3/3 community=20]
NODE Almut Hintze [src=raw/ocr/2008_2009_Avestan_Literature_In_Ronald_E.md loc=chunk 1/3 community=8]
NODE Argument: Avestan orality, recomposition in performance, and ritual crystallization (Nagy 1996; Bakker 1997; Skjærvø 2005–2006) [src=raw/ocr/Abar_Rodestan_i_Babel_The_Zoroastrian_Tr.md loc=chunk 1/3 community=5]
NODE Third-Wave Patronage Migration Argument: loss of Safavid patronage and Mughal demand [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 2/3 community=23]
NODE Farrukh Beyg's departure to India and Mughal-court arrival, c. 1585 [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 3/3 community=23]
NODE Pahlavi Videvdad: Pollution/Purification Legal Zand [src=raw/ocr/Abar_Rodestan_i_Babel_The_Zoroastrian_Tr.md loc=chunk 2/3 community=5]
NODE Mughal Library-Atelier and School of Painting [src=raw/ocr/Between_the_Safavids_and_the_Mughals_Art.md loc=chunk 1/3 community=23]
NODE Videvdad 5.4 Pollution Formula: Order Destroyed, Souls Howling, Bodies Forfeit [src=raw/ocr/Abar_Rodestan_i_Babel_The_Zoroastrian_Tr.md loc=chunk 2/3 community=5]
NODE Claim: Abraham–Zarathustra Syncretic Association [src=raw/ocr/Abraham_and_Nimrod_in_the_Shadow_of_Zar.md loc=chunk 3/3 community=20]
NODE Old Avesta Intertexts (YH 36.6–7; Gāthā 51.22, 51.13, 53.8–9) [src=raw/ocr/Abar_Rodestan_i_Babel_The_Zoroastrian_Tr.md loc=chunk 2/3 community=5]
NODE Muḥammadī [src=raw/oc
... (truncated to ~1600 token budget)
```

### Cognee

- Exit status: `0`
- Runtime: `24.0s`
- Command: `.venv/bin/cognee-zoro query 'What connections does the corpus draw between Zoroastrianism and Jewish eschatology or Second Temple traditions?'`

```text
2026-04-30T22:50:30.999852 [info     ] Deleted old log file: /Users/ali/.cognee/logs/2026-04-30_14-28-31.log [cognee.shared.logging_utils]

2026-04-30T22:50:31.000537 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-50-30.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-50-30.log

2026-04-30T22:50:31.000950 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:50:31.001518 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:50:31.001911 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:50:38.475343 [info     ] Loaded JSON extension          [cognee.shared.logging_utils]

2026-04-30T22:50:38.969143 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-50-30.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-50-30.log

2026-04-30T22:50:38.969500 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:50:38.970163 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:50:38.970532 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:50:44.104982 [info     ] Vector collection retrieval completed: Retrieved distances from 6 collections in 0.31s [cognee.shared.logging_utils]

2026-04-30T22:50:44.106995 [info     ] Retrieving ID-filtered graph from database. [CogneeGraph]

2026-04-30T22:50:44.832761 [info     ] ID-filtered retrieval: 2535 nodes and 3956 edges in 0.73s [cognee.shared.logging_utils]

2026-04-30T22:50:45.407499 [info     ] Graph projection completed: 2535 nodes, 3956 edges in 0.57s [CogneeGraph]

2026-04-30T22:50:45.468477 [info     ] Completed resolving edges to text [cognee.shared.logging_utils] extra={'node_count': 13, 'connection_count': 10}
The corpus hints at significant connections between Zoroastrianism and Jewish eschatology, particularly through concepts of shared liturgies and beliefs in resurrection, judgment after death, and duality in moral and cosmic struggles. It details how both religious traditions may have influenced each other during the Second Temple period, partly due to cultural exchanges and theological dialogues. For instance, Jewish eschatological ideas on resurrection and judgment are seen as evolving during the Babylonian Exile, in parallel with Zoroastrian concepts of individual responsibility and the struggle against evil. Furthermore, specific motifs such as the fiery trials of figures like Abraham and Zarathustra resonate across both traditions, suggesting deeper intertextual and thematic connections.
```

## Winged Disk

Question: What is the debate around the winged disk, Farvahar, Ahura Mazda, and khvarnah?

### Graphify

- Exit status: `0`
- Runtime: `0.6s`
- Command: `graphify query 'What is the debate around the winged disk, Farvahar, Ahura Mazda, and khvarnah?' --graph graphify-out/graph.json --budget 1600`

```text
NODE Dialogue Between Cultures & Exchange of Knowledge And Cultural Ideas [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=None community=7]
NODE Bulletin of the Asia Institute [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=None community=12]
NODE **THE AURA OF KINGS** [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=None community=1]
NODE MORE THAN MEN, LESS THAN GODS [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=None community=17]
NODE By the Favor of Auramazdā: Kingship and the Divine in the Early Achaemenid Period [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Aniconism in the Religious Art of Pre-Islamic Iran and Central Asia [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE Khvarnah / Farr (Divine Glory) [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=None community=2]
NODE Ahura-Mazda [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Darius I [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 1/3 community=17]
NODE Cultural Remnants of Ancient Iran in Turkish Classical Works of the XI-XII Centuries [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Claim: Indo-Iran bilateral relations are ancient, continuous, and worth preserving [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 3/3 community=7]
NODE Indo-Iranian cultural and knowledge exchange [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Sasanian Dynasty [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Darius I's Imperial Program in Texts and Images [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Apam Napāt [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Argument: Ancient Iranian Culture Shaped XI-XII c. Turkish Classical Works after Islam [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Argument: Iranian Aniconism Includes Multiple Categories and Tension between Aniconic Symbols and Anthropomorphic Divine Conceptions [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE Early Achaemenid Kingship and the Divine [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Anthropomorphic Mental Notions of the Divine [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 3/3 community=12]
NODE Winged Symbol / Figure in the Winged Ring [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 2/3 community=17]
NODE Persepolitan Glyptic [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 3/3 community=17]
NODE Winged-Disk, Falcon-Feather, Lotus, and Sunflower Iconography [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE PFS 389* Old Persian Inscription “Dārayaush Pārsā” with Winged Sun Disk [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 3/3 community=17]
NODE Achaemenid/Darius Dual Legitimacy Symbolism [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Material Aniconism: Zoomorphic Symbols, Empty-Space Aniconism, and Elemental Aniconism [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 3/3 community=12]
NODE Material Aniconism [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE Argument: Persia/Iran as intermediary for East–West cultural transmission [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Achaemenid Royal Ideology [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 2/3 community=17]
NODE Abolfazl Khatibi's Shahnameh-Minoye Kherad Comparison [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE T. D. N. Mettinger’s Aniconism Framework, including No Graven Image? [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE Minoye Kherad / Minouch of Wisdom [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Kushan and Sogdian Anthropomorphization of Iranian Deities [src=raw/ocr/Aniconism_
... (truncated to ~1600 token budget)
```

### Cognee

- Exit status: `0`
- Runtime: `31.7s`
- Command: `.venv/bin/cognee-zoro query 'What is the debate around the winged disk, Farvahar, Ahura Mazda, and khvarnah?'`

```text
2026-04-30T22:50:55.633538 [info     ] Deleted old log file: /Users/ali/.cognee/logs/2026-04-30_14-28-49.log [cognee.shared.logging_utils]

2026-04-30T22:50:55.634243 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-50-55.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-50-55.log

2026-04-30T22:50:55.634663 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:50:55.634925 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:50:55.635185 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:51:03.334050 [info     ] Loaded JSON extension          [cognee.shared.logging_utils]

2026-04-30T22:51:03.918484 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-50-55.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-50-55.log

2026-04-30T22:51:03.918890 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:51:03.919197 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:51:03.919468 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:51:09.555033 [info     ] Vector collection retrieval completed: Retrieved distances from 6 collections in 0.32s [cognee.shared.logging_utils]

2026-04-30T22:51:09.556114 [info     ] Retrieving ID-filtered graph from database. [CogneeGraph]

2026-04-30T22:51:10.340670 [info     ] ID-filtered retrieval: 2541 nodes and 4137 edges in 0.78s [cognee.shared.logging_utils]

2026-04-30T22:51:10.968045 [info     ] Graph projection completed: 2541 nodes, 4137 edges in 0.63s [CogneeGraph]

2026-04-30T22:51:11.026762 [info     ] Completed resolving edges to text [cognee.shared.logging_utils] extra={'node_count': 12, 'connection_count': 10}
The debate around the winged disk, Farvahar, Ahura Mazdā, and khvarnah centers on their symbolism and interpretations in Zoroastrianism and Iranian culture. Key points include:

1. **Symbol Associations**: The winged disk is often interpreted as a symbol of Ahura Mazdā, the supreme deity in Zoroastrianism. Alternatively, it can represent khvarnah, a concept of divine glory and authority associated with kingship and success.

2. **Different Ideologies**: Scholars like Lecoq argue whether the winged disk symbolizes Ahura Mazdā or khvarnah, suggesting that it derived from different ideological backgrounds—Achaemenid vs. pre-Achaemenid traditions.

3. **Inclusion of Deities**: The imagery often blends representations of Ahura Mazdā with local traditions, as seen in depictions where a king receives the ring of investiture from Ahura Mazdā, showcasing the interconnectedness of divine authority and royal legitimacy.

4. **Historical Transitions**: The shift in cultural emphasis from earlier sun and water deities (like Mithrā and Apam-Napāt) to Ahura Mazdā reflects political necessities during the Achaemenid transition, highlighting the need for legitimacy and divine approval.

5. **Mithraic Influence**: The integration of elements associated with Mithrā, who was revered and depicted with similar symbols, complicates the understanding of who held authority over khvarnah, with debates indicating that even post-Zoroastrian reforms, remnants of Mithraism persisted in popular belief.

Overall, the debate illustrates how symbolism and meanings have evolved, influenced by historical, cultural, and religious dynamics in ancient Iran.
```

## Sasanian Kingship

Question: What does the corpus say about Sasanian kingship, investiture, divine sanction, and legitimacy?

### Graphify

- Exit status: `0`
- Runtime: `0.5s`
- Command: `graphify query 'What does the corpus say about Sasanian kingship, investiture, divine sanction, and legitimacy?' --graph graphify-out/graph.json --budget 1600`

```text
NODE CONCEPTS OF POLLUTION IN LATE SASANIAN IRAN DOES POLLUTION NEED STAIRS, AND DOES IT FILL SPACE? [src=raw/ocr/CONCEPTS_OF_POLLUTION_IN_LATE_SASANIAN_I.md loc=None community=13]
NODE Bulletin of the Asia Institute [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=None community=12]
NODE MORE THAN MEN, LESS THAN GODS [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=None community=17]
NODE **THE AURA OF KINGS** [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=None community=1]
NODE --- Monotheism the Zoroastrian Way [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=None community=22]
NODE Ancient Iran: Cosmology, Mythology, History [src=raw/ocr/Ancient_Iran_Cosmology_Mythology_History.md loc=None community=2]
NODE Ahura Mazdā [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE By the Favor of Auramazdā: Kingship and the Divine in the Early Achaemenid Period [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Aniconism in the Religious Art of Pre-Islamic Iran and Central Asia [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE Ahura Mazdā / Ohrmazd [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=chunk 1/3 community=22]
NODE Khvarnah / Farr (Divine Glory) [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Zoroastrianism [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=chunk 1/3 community=22]
NODE Mazdian Cosmology [src=raw/ocr/Ancient_Iran_Cosmology_Mythology_History.md loc=chunk 1/3 community=2]
NODE Khvarnah / Farr (Iranian Royal Glory) [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 3/3 community=1]
NODE Darius I [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 1/3 community=17]
NODE Angra Mainyu / Ahreman [src=raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md loc=chunk 1/3 community=22]
NODE Corpse-Pollution [src=raw/ocr/CONCEPTS_OF_POLLUTION_IN_LATE_SASANIAN_I.md loc=chunk 1/3 community=13]
NODE Claim: tuhīgīh as Empty-Space Pollution Occupying Consolidated Three-Dimensional Space [src=raw/ocr/CONCEPTS_OF_POLLUTION_IN_LATE_SASANIAN_I.md loc=chunk 3/3 community=13]
NODE Darius I's Imperial Program in Texts and Images [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Apam Napāt [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Farr / Khvarnah (Divine Glory) [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Argument: Iranian Aniconism Includes Multiple Categories and Tension between Aniconic Symbols and Anthropomorphic Divine Conceptions [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE Early Achaemenid Kingship and the Divine [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Winged Symbol / Figure in the Winged Ring [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 2/3 community=17]
NODE Pahlavi Videvdad [src=raw/ocr/CONCEPTS_OF_POLLUTION_IN_LATE_SASANIAN_I.md loc=chunk 2/3 community=13]
NODE Anthropomorphic Mental Notions of the Divine [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 3/3 community=12]
NODE Daštānestān Menstrual Hut Pollution Case (TD2 p. 573) [src=raw/ocr/CONCEPTS_OF_POLLUTION_IN_LATE_SASANIAN_I.md loc=chunk 3/3 community=13]
NODE Concepts of Pollution in Late Sasanian Iran: Does Pollution Need Stairs, and Does It Fill Space? [src=raw/ocr/CONCEPTS_OF_POLLUTION_IN_LATE_SASANIAN_I.md loc=chunk 1/3 community=13]
NODE Achaemenid Winged-Disk Symbolism Debate [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Material Aniconism: Zoomorphic Symbols, Empty-Space Aniconism, and Elemental Aniconism [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 3/3 community=12]
NODE Argument: Mithrā and Apam-Napāt Embodied Median Kingly Power [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 2/3 community=1]
NODE Material Aniconism [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE Contact Transmission of Corpse Pollution [src=raw/ocr/CONCEPTS_OF_POLLUTION_IN_LATE_SASANIAN_I.md loc=chunk 2/3 community=13]
NODE PFS 389* Old Persian Inscription “Dārayaush Pārsā” with Winged Sun Disk [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 3/3 community=17]
NODE Argument: Dual Legitimacy Symbolism [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 3/3 community=1]
NODE Imperial Program in the Visual Arts during the Reign
... (truncated to ~1600 token budget)
```

### Cognee

- Exit status: `0`
- Runtime: `27.5s`
- Command: `.venv/bin/cognee-zoro query 'What does the corpus say about Sasanian kingship, investiture, divine sanction, and legitimacy?'`

```text
2026-04-30T22:51:27.904533 [info     ] Deleted old log file: /Users/ali/.cognee/logs/2026-04-30_14-51-13.log [cognee.shared.logging_utils]

2026-04-30T22:51:27.905072 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-51-27.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-51-27.log

2026-04-30T22:51:27.906290 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:51:27.907280 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:51:27.907736 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:51:34.919150 [info     ] Loaded JSON extension          [cognee.shared.logging_utils]

2026-04-30T22:51:35.462737 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-51-27.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-51-27.log

2026-04-30T22:51:35.463592 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:51:35.464185 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:51:35.464541 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:51:40.774377 [info     ] Vector collection retrieval completed: Retrieved distances from 6 collections in 0.30s [cognee.shared.logging_utils]

2026-04-30T22:51:40.775912 [info     ] Retrieving ID-filtered graph from database. [CogneeGraph]

2026-04-30T22:51:41.607311 [info     ] ID-filtered retrieval: 2613 nodes and 4220 edges in 0.83s [cognee.shared.logging_utils]

2026-04-30T22:51:42.249436 [info     ] Graph projection completed: 2613 nodes, 4220 edges in 0.64s [CogneeGraph]

2026-04-30T22:51:42.305791 [info     ] Completed resolving edges to text [cognee.shared.logging_utils] extra={'node_count': 16, 'connection_count': 10}
The corpus discusses Sasanian kingship as a system deeply rooted in the ideology of divine sanction and legitimacy. It emphasizes the connection between the Sasanian rulers and divine authority, particularly through visual representations and inscriptions asserting that kingship was divinely conferred and maintained through righteousness. The concept of "chihr," symbolizing the reflective image or glory of the divine, is crucial, suggesting that rulers represented the image of the gods and held the responsibility to reflect divine qualities. These notions were visually articulated in rock reliefs and inscriptions where kings were depicted alongside deities, reinforcing their legitimacy and authority, which was perceived as temporary and contingent upon their conduct. Arbiter of both temporal and spiritual realms, the Sasanian monarch's role encompassed safeguarding Zoroastrian traditions while claiming divine favor by emphasizing their lineage and connection to the gods.
```

## Anahita / Apam Napat

Question: What role do Anahita and Apam Napat play in the corpus, especially around kingship or divine power?

### Graphify

- Exit status: `0`
- Runtime: `0.6s`
- Command: `graphify query 'What role do Anahita and Apam Napat play in the corpus, especially around kingship or divine power?' --graph graphify-out/graph.json --budget 1600`

```text
NODE ASTYAGES, CYRUS AND ZOROASTER: SOLVING A HISTORICAL DILEMMA [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=None community=3]
NODE **THE AURA OF KINGS** [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=None community=1]
NODE MORE THAN MEN, LESS THAN GODS [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=None community=17]
NODE Ancient Iran: Cosmology, Mythology, History [src=raw/ocr/Ancient_Iran_Cosmology_Mythology_History.md loc=None community=2]
NODE Ahura Mazdā [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE By the Favor of Auramazdā: Kingship and the Divine in the Early Achaemenid Period [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Avesta [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=3]
NODE Ahura-Mazda [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=None community=2]
NODE Khvarnah / Farr (Divine Glory) [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=None community=2]
NODE Khvarnah / Farr (Iranian Royal Glory) [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 3/3 community=1]
NODE Darius I [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 1/3 community=17]
NODE Mazdian Cosmology [src=raw/ocr/Ancient_Iran_Cosmology_Mythology_History.md loc=chunk 1/3 community=2]
NODE Darius I's Imperial Program in Texts and Images [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Apam Napāt [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Farr / Khvarnah (Divine Glory) [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Khvarenah [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Winged Symbol / Figure in the Winged Ring [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 2/3 community=17]
NODE Achaemenid Winged-Disk Symbolism Debate [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Astyages Banished Zoroaster Hypothesis [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 1/3 community=3]
NODE Khvarnah / Farr [src=raw/ocr/Ancient_Iran_Cosmology_Mythology_History.md loc=chunk 2/3 community=2]
NODE Early Achaemenid Kingship and the Divine [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE François Vallat's Achaemenid Lineage and Banishment Thesis (Vallat 2010; 2011) [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 1/3 community=3]
NODE Pasargadae Rehabilitated: Authenticity of Cyrus' Inscriptions and Reliefs [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 2/3 community=3]
NODE Cyrus, Darius, and Achaemenid Ideology [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Achaemenid Royal Ideology [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 2/3 community=17]
NODE Avestan Priestly Redaction Thesis [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 3/3 community=3]
NODE Winged-Disk, Falcon-Feather, Lotus, and Sunflower Iconography [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Argument: Mithrā and Apam-Napāt Embodied Median Kingly Power [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 2/3 community=1]
NODE Argument: Dual Legitimacy Symbolism [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 3/3 community=1]
NODE Median Magi, Magophonia, and Kingly Ideology [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 3/3 community=3]
NODE Zoroaster / Zarathushtra [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 1/3 community=3]
NODE Achaemenid/Darius Dual Legitimacy Symbolism [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Lotus-Sunflower Dual Khvarnah Symbolism [src=raw
... (truncated to ~1600 token budget)
```

### Cognee

- Exit status: `0`
- Runtime: `30.8s`
- Command: `.venv/bin/cognee-zoro query 'What role do Anahita and Apam Napat play in the corpus, especially around kingship or divine power?'`

```text
2026-04-30T22:51:56.173897 [info     ] Deleted old log file: /Users/ali/.cognee/logs/2026-04-30_14-51-44.log [cognee.shared.logging_utils]

2026-04-30T22:51:56.175962 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-51-55.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-51-55.log

2026-04-30T22:51:56.176848 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:51:56.177267 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:51:56.177641 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:52:03.778987 [info     ] Loaded JSON extension          [cognee.shared.logging_utils]

2026-04-30T22:52:04.276087 [info     ] Log file created at: /Users/ali/.cognee/logs/2026-04-30_15-51-55.log [cognee.shared.logging_utils] log_file=/Users/ali/.cognee/logs/2026-04-30_15-51-55.log

2026-04-30T22:52:04.276906 [warning  ] Cognee 1.0 changes: New API — remember/recall/forget/improve (V1 add/cognify/search still work). Session memory enabled by default (CACHING=false to disable). Multi-user access control on by default (ENABLE_BACKEND_ACCESS_CONTROL=false to disable). Agents (@cognee.agent) auto-verified on registration. See https://docs.cognee.ai/ [cognee.shared.logging_utils]

2026-04-30T22:52:04.277231 [info     ] Logging initialized            [cognee.shared.logging_utils] cognee_version=1.0.1 database_path=/Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases os_info='Darwin 24.6.0 (Darwin Kernel Version 24.6.0: Mon Oct 27 21:13:29 PDT 2025; root:xnu-11417.140.69.703.14~2/RELEASE_X86_64)' python_version=3.11.8 structlog_version=25.5.0

2026-04-30T22:52:04.277617 [info     ] Database storage: /Users/ali/COGNEE-zoroastrianism/data-root/cognee-system/databases [cognee.shared.logging_utils]

2026-04-30T22:52:09.734552 [info     ] Vector collection retrieval completed: Retrieved distances from 6 collections in 0.27s [cognee.shared.logging_utils]

2026-04-30T22:52:09.735996 [info     ] Retrieving ID-filtered graph from database. [CogneeGraph]

2026-04-30T22:52:10.532252 [info     ] ID-filtered retrieval: 2419 nodes and 3810 edges in 0.80s [cognee.shared.logging_utils]

2026-04-30T22:52:11.152395 [info     ] Graph projection completed: 2419 nodes, 3810 edges in 0.62s [CogneeGraph]

2026-04-30T22:52:11.214986 [info     ] Completed resolving edges to text [cognee.shared.logging_utils] extra={'node_count': 15, 'connection_count': 10}
In the corpus, Anahita and Apam Napāt are portrayed as significant deities in relation to kingship and divine power. Apam Napāt, associated with water and often represented as a protector of khvarnah (divine glory), was entrusted with promoting authority and suppressing rebellions, particularly during the time of Zoroaster's influence. Anahita, associated with fertility and waters, later absorbed some of Apam Napāt's attributes, becoming a powerful goddess in her own right. 

Both deities were considered crucial in the royal iconography of the Achaemenids, symbolizing divine blessing and legitimacy for rulers. For instance, representations of Anahita in conjunction with Apam Napāt are found in royal imagery, emphasizing their roles in conferring authority and ensuring a ruler's success and well-being. Their duality reflects a synthesis of earlier beliefs in authority connected to both aquatic and solar elements, with Apam Napāt representing the nighttime and Anahita representing fertility and prosperity in the daytime.
```
