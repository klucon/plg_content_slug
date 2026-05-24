# plg_content_slug

Plugin pro doplňkovou normalizaci slugů obsahu.

## Metadata

| Pole | Hodnota |
| :--- | :--- |
| Typ | `plugin` |
| Verze | `0.1.0` |
| Vendor | `klucon` |
| Extension ID | `klucon/plg_content_slug` |
| Kategorie | `content` |
| Licence | MIT |
| Core minimum | `0.2.15` |
| Python | `>=3.12` |
| Entry point | `src.plugins.plg_content_slug` |
| Repository | `https://github.com/klucon/plg_content_slug` |

## Účel

Plugin poslouchá hook `content.article.saved` a umí doplnit slug podle titulku, pokud článek dorazí bez slug hodnoty. Základní `com_content` už slug vytváří v service vrstvě, plugin je připravený jako samostatná pojistka a budoucí místo pro redirect historii.

## Poznámky k verzi

První verze s jednotným podpisem `setup(registry)` a GitHub manifest metadaty.
