string = "SettingsHistoryID, ShiftRunID, OrderID, CalendarID, ItemID, CustomerID, ProdCategoryDetailID, LineID, FacilityID, RecipeID, ProdStart, ProdEnd, ProdDuration, BoxCount, FillerTotalTills, FillerTPM, FillerTotalGrams, AnritsuTotalTills, AnritsuTotalGrams, AnritsuPass, AnritsuUnder, AnritsuDouble, AnritsuMetal, AnritsuMean, AnritsuSD, LabourCount, InfeedRate, UVActual, LabelScannerEnabled GoodLabelScans, BadLabelScans, NoLabelScans, PTIScannerEnabled, GoodPTIScans, BadPTIScans, NoPTIScans, FacilityDWVersion"


columns = string.split(" ")
formatted_columns = ''

for column in columns:
    column = 's.' + column
    formatted_columns = formatted_columns + ' ' + column

print(formatted_columns)