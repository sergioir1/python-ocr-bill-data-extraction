annotators = {
    "luz": [
        {
            "name": "ANNOTATOR__001", #P1 power total price
            "regex": r'(\d{1,3}\,\d{2})\s\€\sP1\s(\d*\,\d*)\skW\sx\s(\d*\sD[ií]as)\sx\s(\d*\,\d*)\s\€\/kW\sdía',
            "precedence": 1,
            "rewrite": r"\s"
        },
        {
            "name": "ANNOTATOR__002", #P3 power total price
            "regex": r'(\d{1,3}\,\d{2})\s\€\sP3\s(\d*\,\d*)\skW\sx\s(\d*\sD[ií]as)\sx\s(\d*\,\d*)\s\€\/kW\sdía',
            "precedence": 1,
            "rewrite": r"\s"
        }
    ]
}