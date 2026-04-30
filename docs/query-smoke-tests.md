# Graphify Query Smoke Tests

- Generated at: 2026-04-30T21:12:04Z
- Graph: `graphify-out/graph.json`
- Input: `graphify-input/ocr-markdown-clean`
- Purpose: verify the finalized Graphify graph is queryable after the clean deduped rebuild.

## Mithra / Mithras Connections

- Exit status: `0`

```text
$ .venv/bin/graphify query What\ does\ this\ corpus\ connect\ Mithra\ or\ Mithras\ to\? --graph graphify-out/graph.json
NODE 02239118 [src=raw/ocr/02239118.md loc=None community=25]
NODE York/Micklegate Bas-relief of Mithras (dug up 1747) [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Account of a Bas-relief of Mithras Found at York [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Mithriac Ceremonies and Mysteries [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Inference: Roman Prefect of York Demolished a Subterranean Mithras Temple in Micklegate [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Mithras [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Tertullian, c. 40 on Mithriac Baptism, Forehead Cross, and Bread [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE St. Jerome, Epistle to Laeta: Gracchus Destroys the Cave of Mithras [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Argument: Patriarchal Religion as Christianity Antedated [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Solar and Zodiacal Symbolism of Mithras Reliefs [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE James Mounsey Letter to Henry Baker (Riga, 1749) [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Rev. Dr. William Stukeley, F.R.S. [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
NODE Russia Castor, Carlsbad Baths, and Cracau Salt-mines [src=raw/ocr/02239118.md loc=chunk 1/1 community=25]
EDGE Mithras --references [EXTRACTED]--> 02239118
EDGE Mithras --participates_in [EXTRACTED]--> Mithriac Ceremonies and Mysteries
EDGE York/Micklegate Bas-relief of Mithras (dug up 1747) --references [EXTRACTED]--> 02239118
EDGE York/Micklegate Bas-relief of Mithras (dug up 1747) --references [EXTRACTED]--> Account of a Bas-relief of Mithras Found at York
EDGE York/Micklegate Bas-relief of Mithras (dug up 1747) --conceptually_related_to [EXTRACTED]--> Mithriac Ceremonies and Mysteries
EDGE St. Jerome, Epistle to Laeta: Gracchus Destroys the Cave of Mithras --references [EXTRACTED]--> 02239118
EDGE St. Jerome, Epistle to Laeta: Gracchus Destroys the Cave of Mithras --cites [EXTRACTED]--> Account of a Bas-relief of Mithras Found at York
EDGE Solar and Zodiacal Symbolism of Mithras Reliefs --references [EXTRACTED]--> 02239118
EDGE Solar and Zodiacal Symbolism of Mithras Reliefs --conceptually_related_to [EXTRACTED]--> Mithriac Ceremonies and Mysteries
EDGE Inference: Roman Prefect of York Demolished a Subterranean Mithras Temple in Micklegate --references [EXTRACTED]--> 02239118
EDGE Inference: Roman Prefect of York Demolished a Subterranean Mithras Temple in Micklegate --references [EXTRACTED]--> Account of a Bas-relief of Mithras Found at York
EDGE Account of a Bas-relief of Mithras Found at York --participates_in [EXTRACTED]--> Rev. Dr. William Stukeley, F.R.S.
EDGE Account of a Bas-relief of Mithras Found at York --cites [EXTRACTED]--> Tertullian, c. 40 on Mithriac Baptism, Forehead Cross, and Bread
EDGE 02239118 --references [EXTRACTED]--> Argument: Patriarchal Religion as Christianity Antedated
EDGE 02239118 --references [EXTRACTED]--> James Mounsey Letter to Henry Baker (Riga, 1749)
EDGE 02239118 --references [EXTRACTED]--> Rev. Dr. William Stukeley, F.R.S.
EDGE 02239118 --references [EXTRACTED]--> Russia Castor, Carlsbad Baths, and Cracau Salt-mines
EDGE 02239118 --references [EXTRACTED]--> Tertullian, c. 40 on Mithriac Baptism, Forehead Cross, and Bread
EDGE Mithriac Ceremonies and Mysteries --conceptually_related_to [EXTRACTED]--> Argument: Patriarchal Religion as Christianity Antedated
```

## Ahura Mazda Explanation

- Exit status: `0`

```text
$ .venv/bin/graphify explain $'Ahura Mazd�\201' --graph graphify-out/graph.json
Node: Ahura Mazdā / Ohrmazd
  ID:        llm_ahura_mazd_ohrmazd
  Source:    raw/ocr/2014_Monotheism_the_Zoroastrian_Way_Jour.md chunk 1/3
  Type:      document
  Community: 22
  Degree:    13

Connections (13):
  --> --- Monotheism the Zoroastrian Way [references] [EXTRACTED]
  --> Zoroastrianism [participates_in] [EXTRACTED]
  --> Angra Mainyu / Ahreman [contrasts_with] [EXTRACTED]
  --> Material Creation (gētīy; Ahura Mazdā’s world) [conceptually_related_to] [EXTRACTED]
  --> Spənta Mainiiu and Amesha Spentas (Life-Giving Immortals) [conceptually_related_to] [EXTRACTED]
  --> Yazatas as 'Worthy of Worship' (aoxtō.nāmana yasna) [conceptually_related_to] [EXTRACTED]
  --> Spiritual Creation [conceptually_related_to] [EXTRACTED]
  --> Zoroastrian Creation Myth [participates_in] [EXTRACTED]
  --> Ahura Mazdā's Omniscience over Omnipotence [conceptually_related_to] [EXTRACTED]
  --> Yazatas, Spiritual and Material Objects of Worship [conceptually_related_to] [EXTRACTED]
  --> Mazdayasnians / Zoroastrians [conceptually_related_to] [EXTRACTED]
  --> Spiritual Creation (mēnōy; forms/kirb) [conceptually_related_to] [EXTRACTED]
  --> Vīdēvdād Purity Laws [conceptually_related_to] [EXTRACTED]
```

## Mithra To Ahura Mazda Path

- Exit status: `0`

```text
$ .venv/bin/graphify path Mithra $'Ahura Mazd�\201' --graph graphify-out/graph.json
Shortest path (4 hops):
  Mithraic Solar-Serpent-Lion Iconography (Sasanian Seals and Armenian Mehean Portals) --conceptually_related_to [EXTRACTED]--> Apam Napāt --references [EXTRACTED]--> **THE AURA OF KINGS** --references [EXTRACTED]--> Ahura Mazdā --conceptually_related_to [EXTRACTED]--> Yasna Haptaṅhāiti Fire Ritual and Ahura Mazdā's Presence (Y. 34.4; Y. 36.2–6)
```

## Khvarnah / Farr Royal Glory

- Exit status: `0`

```text
$ .venv/bin/graphify query What\ does\ the\ graph\ say\ about\ Khvarnah\,\ Farr\,\ royal\ glory\,\ and\ kingship\? --graph graphify-out/graph.json
NODE Dialogue Between Cultures & Exchange of Knowledge And Cultural Ideas [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=None community=7]
NODE Contribution of Persia to the World Civilization [src=raw/ocr/50263688-Contribution-of-Persia-to-the-World-Civilization-doc-XP.md loc=None community=0]
NODE **THE AURA OF KINGS** [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=None community=1]
NODE Gifts to a Magus [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=None community=1]
NODE Ahura Mazdā [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Zarathustra [src=raw/ocr/2008_2009_Avestan_Literature_In_Ronald_E.md loc=chunk 1/3 community=1]
NODE Ahura-Mazda [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=None community=2]
NODE Khvarnah / Farr (Divine Glory) [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Argument: Persian 'firsts' and 'greatest' contributions to Islamic sciences and world civilization [src=raw/ocr/50263688-Contribution-of-Persia-to-the-World-Civilization-doc-XP.md loc=chunk 3/3 community=0]
NODE Contribution of Persia to the World Civilization [src=raw/ocr/50263688-Contribution-of-Persia-to-the-World-Civilization-doc-XP.md loc=chunk 1/3 community=0]
NODE Claim: Indo-Iran bilateral relations are ancient, continuous, and worth preserving [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 3/3 community=7]
NODE Persia / Greater Persia [src=raw/ocr/50263688-Contribution-of-Persia-to-the-World-Civilization-doc-XP.md loc=chunk 2/3 community=0]
NODE Cultural Remnants of Ancient Iran in Turkish Classical Works of the XI-XII Centuries [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Zarathustra’s Prophetic and Priestly Authority [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Women Priests and Charismatic Gender-Inclusive Authority [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 3/3 community=1]
NODE Sasanian Dynasty [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Argument: Persian Civilization as Source of World Civilization [src=raw/ocr/50263688-Contribution-of-Persia-to-the-World-Civilization-doc-XP.md loc=chunk 1/3 community=0]
NODE Indo-Iranian cultural and knowledge exchange [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Apam Napāt [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Visible citations: Parsi Names; Persian Letters; International Herald Tribune; BBC; History Channel [src=raw/ocr/50263688-Contribution-of-Persia-to-the-World-Civilization-doc-XP.md loc=chunk 3/3 community=0]
NODE Persian Empire [src=raw/ocr/471689884-Contribution-of-Persia-to-the-World-Civilization-2019-doc-doc.md loc=chunk 1/3 community=0]
NODE Professor Arthur A. Pope [src=raw/ocr/471689884-Contribution-of-Persia-to-the-World-Civilization-2019-doc-doc.md loc=chunk 1/3 community=0]
NODE Argument: Ancient Iranian Culture Shaped XI-XII c. Turkish Classical Works after Islam [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Article Argument: Zarathustra’s Prophetic and Priestly Authority (Max Weber Typology) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 2/3 community=1]
NODE Other visible cited sources: Iran: Land and the People; National Geographic Channel; Parsi Names; IHT; Webster/Insight/DK; BBC/Discovery/PDI; Village Voice/Nehru [src=raw/ocr/50263688-Contribution-of-Persia-to-the-World-Civilization-doc-XP.md loc=chunk 2/3 community=0]
NODE Cyrus the Great of Persia [src=raw/ocr/471689884-Contribution-of-Persia-to-the-World-Civilization-2019-doc-doc.md loc=chunk 1/3 community=0]
NODE Dual Prophetic-Priestly Authority of Zarathustra [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 3/3 community=1]
NODE Persian Human Rights Charters (Ganj-Nameh and Cyrus baked-clay tablet) [src=raw/ocr/50263688-Contribution-of-Persia-to-the-World-Civilization-doc-XP.md loc=chunk 1/3 community=0]
NODE Winged-Disk, Falcon-Feather, Lotus, and Sunflower Iconography [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Abolfazl Khatibi's Shahnameh-Minoye Kherad Comparison [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Minoye Kherad / Minouch of Wisdom [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 2/3 community=7]
NODE Achaemenid/Darius Dual Legitimacy Symbolism [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Caliph Al-Ma'mun and the House of Wisdom in Baghdad [src=raw/ocr/471689884-Contribution-of-Persia-to-the-World-Civilization-2019-doc-doc.md loc=chunk 3/3 community=0]
NODE Lotus-Sunflower Dual Khvarnah Symbolism [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 2/3 community=1]
NODE Zoroastrianism / Mazdayasnian Religion (daēnā mazdayasni; MK fol. 19v.1–4) [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE Argument: Persia/Iran as intermediary for East–West cultural transmission [src=raw/ocr/Arta_and_Asa_in_proper_names_and_the_ran.md loc=chunk 1/3 community=7]
NODE Zoroaster's Reforms and Late-7th-Century Dating Argument [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Gardeshgari (Iran perio
... (truncated to ~2000 token budget)
```

## Sasanian Kingship

- Exit status: `0`

```text
$ .venv/bin/graphify query What\ does\ the\ graph\ say\ about\ Sasanian\ kingship\,\ divine\ sanction\,\ and\ legitimacy\? --graph graphify-out/graph.json
NODE Bulletin of the Asia Institute [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=None community=12]
NODE MORE THAN MEN, LESS THAN GODS [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=None community=17]
NODE **THE AURA OF KINGS** [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=None community=1]
NODE Ahura Mazdā [src=raw/ocr/69_On_the_Prophetic_and_Priestly_Authori.md loc=chunk 1/3 community=1]
NODE By the Favor of Auramazdā: Kingship and the Divine in the Early Achaemenid Period [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Aniconism in the Religious Art of Pre-Islamic Iran and Central Asia [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=None community=2]
NODE Ahura-Mazda [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Khvarnah / Farr (Divine Glory) [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Darius I [src=raw/ocr/Astyages_Cyrus_and_Zoroaster_Solving_a_H.md loc=chunk 1/3 community=17]
NODE Khvarnah / Farr (Iranian Royal Glory) [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 3/3 community=1]
NODE Farr / Khvarnah (Divine Glory) [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Darius I's Imperial Program in Texts and Images [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Apam Napāt [src=raw/ocr/Academia Summary — MITHRAIC SOCIETIES: FROM BROTHERHOOD IDEAL TO RELIGION'S ADVERSARY .md loc=chunk 1/1 community=2]
NODE Argument: Iranian Aniconism Includes Multiple Categories and Tension between Aniconic Symbols and Anthropomorphic Divine Conceptions [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE Early Achaemenid Kingship and the Divine [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 1/3 community=17]
NODE Achaemenid Winged-Disk Symbolism Debate [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Anthropomorphic Mental Notions of the Divine [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 3/3 community=12]
NODE Winged Symbol / Figure in the Winged Ring [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 2/3 community=17]
NODE The Aura of Kings: Legitimacy and Divine Sanction in Iranian Kingship [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Achaemenid/Darius Dual Legitimacy Symbolism [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Lotus-Sunflower Dual Khvarnah Symbolism [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 2/3 community=1]
NODE Material Aniconism: Zoomorphic Symbols, Empty-Space Aniconism, and Elemental Aniconism [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 3/3 community=12]
NODE Winged-Disk, Falcon-Feather, Lotus, and Sunflower Iconography [src=raw/ocr/Academia Summary — Aura of Kings; Legitimacy and Divine Sanction in Iranian Kingship .md loc=chunk 1/1 community=2]
NODE Kushan and Sogdian Anthropomorphization of Iranian Deities [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 2/3 community=12]
NODE T. D. N. Mettinger’s Aniconism Framework, including No Graven Image? [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE Material Aniconism [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE Tower Structure Iconography [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 2/3 community=17]
NODE Argument: Dual Legitimacy Symbolism [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 3/3 community=1]
NODE Argument: Mithrā and Apam-Napāt Embodied Median Kingly Power [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 2/3 community=1]
NODE The Aura of Kings [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 3/3 community=1]
NODE Argument: Mesopotamian Heritage Shaped Iranian Aniconism and Anthropomorphism [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 2/3 community=12]
NODE Avesta and Rig Veda as Early Indo-Iranian Religious Texts [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 1/3 community=12]
NODE PFS 389* Old Persian Inscription “Dārayaush Pārsā” with Winged Sun Disk [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 3/3 community=17]
NODE Achaemenid Royal Ideology [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 2/3 community=17]
NODE S. Shahbazi, "An Achemenid Symbol. II. Farnah '(God Given) Fortune' Symbolised" (1980) [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Persepolitan Glyptic [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 3/3 community=17]
NODE Imperial Program in the Visual Arts during the Reign of Darius I [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 3/3 community=17]
NODE Pierre Lecq, "Ahura Mazda ou Xvarnah?" (1984) [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 1/3 community=1]
NODE Mithrā [src=raw/ocr/Aura_of_Kings_Legitimacy_and_Divine_Sanc.md loc=chunk 2/3 community=1]
NODE Partial Figure-ness and Elevation Argument [src=raw/ocr/By_the_Favor_of_Auramazda_Kingship_and.md loc=chunk 2/3 community=17]
NODE Achaemenian Winged Symbol on the Behestūn Relief of Darius I [src=raw/ocr/Aniconism_in_the_Religious_Art_of_Pre_Is.md loc=chunk 3/3 community=12]
NODE PFS 75 Lunar Libation Scene with Crescent and Pedestal A
... (truncated to ~2000 token budget)
```

