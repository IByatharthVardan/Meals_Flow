from typing import Text, Any
import re
import json


goldenData = {
    "w_253593f7838271aee0eaf938c43232a8c98dc25b.jpg": {
        "Filename": "w_253593f7838271aee0eaf938c43232a8c98dc25b.jpg",
        "Total $ amount": "12.1",
        "Date": "06/05/2019",
        "Vendor": "Laura's Lunch Lab"
    },
    "w_14102c3817094bbdbcf5e4f916692ab23075527d.pdf": {
        "Filename": "w_14102c3817094bbdbcf5e4f916692ab23075527d.pdf",
        "Total $ amount": "44.98",
        "Date": "10/04/2018",
        "Vendor": "Uber"
    },
    "w_1df753cb37cf4edc98f1886fcff99fdd031bc7fd.pdf": {
        "Filename": "w_1df753cb37cf4edc98f1886fcff99fdd031bc7fd.pdf",
        "Total $ amount": "50.19",
        "Date": "12/04/2018",
        "Vendor": "Uber"
    },
    "w_1284fd8bb15f7f1528bdb0ee11ec064e9395484e.jpg": {
        "Filename": "w_1284fd8bb15f7f1528bdb0ee11ec064e9395484e.jpg",
        "Total $ amount": "1673",
        "Date": "06/17/2019",
        "Vendor": "Chopt"
    },
    "w_0e91d934f9bd4f00f6921ef9cdb0b96d5a1fa319.pdf": {
        "Filename": "w_0e91d934f9bd4f00f6921ef9cdb0b96d5a1fa319.pdf",
        "Total $ amount": "51.38",
        "Date": "2/6/2019",
        "Vendor": "Uber"
    },
    "w_0fca03faee26e59b80606e96e3ab2f332133648a.pdf": {
        "Filename": "w_0fca03faee26e59b80606e96e3ab2f332133648a.pdf",
        "Total $ amount": "5137",
        "Date": "03/08/2019",
        "Vendor": "Uber"
    },
    "w_13670a5698a0f238d93fb86d2724abe95e125b8e.jpg": {
        "Filename": "w_13670a5698a0f238d93fb86d2724abe95e125b8e.jpg",
        "Total $ amount": "15",
        "Date": "5/29/2019",
        "Vendor": "Kissaten Jin"
    },
    "w_117265e8c005cd48b2d8c5bf41a90a1fe370f24e.jpg": {
        "Filename": "w_117265e8c005cd48b2d8c5bf41a90a1fe370f24e.jpg",
        "Total $ amount": "22.06",
        "Date": "12/17/2018",
        "Vendor": "The Waylon"
    },
    "w_10db54344cec576636c9a300401b4fc1e4811a71.jpg": {
        "Filename": "w_10db54344cec576636c9a300401b4fc1e4811a71.jpg",
        "Total $ amount": "121.4",
        "Date": "04/26/2019",
        "Vendor": "Sigiri"
    },
    "w_142d305ebfd241ea506e694e8472b16aa8afbf03.jpg": {
        "Filename": "w_142d305ebfd241ea506e694e8472b16aa8afbf03.jpg",
        "Total $ amount": "14.63",
        "Date": "06/25/2019",
        "Vendor": "Just Salad"
    },
    "w_160144d30d50472117a5a8e13195b1cf2017b03a.jpg": {
        "Filename": "w_160144d30d50472117a5a8e13195b1cf2017b03a.jpg",
        "Total $ amount": "8.5",
        "Date": "03/26/2019",
        "Vendor": "Ana Maria Mexican Food"
    },
    "w_15f4e03ebeb90ae4e9f22fab509e3b74c6a5873c.jpg": {
        "Filename": "w_15f4e03ebeb90ae4e9f22fab509e3b74c6a5873c.jpg",
        "Total $ amount": "25.2",
        "Date": "02/02/2019",
        "Vendor": "The Beer Hall"
    },
    "w_1c2f81bec8edcb5e0f9572a33876e5e1e155fc2f.pdf": {
        "Filename": "w_1c2f81bec8edcb5e0f9572a33876e5e1e155fc2f.pdf",
        "Total $ amount": "48.55",
        "Date": "02/02/2019",
        "Vendor": "Uber"
    },
    "w_10366662e31b3e775f63e5e5a1beb4ad90fc51a7.pdf": {
        "Filename": "w_10366662e31b3e775f63e5e5a1beb4ad90fc51a7.pdf",
        "Total $ amount": "57.74",
        "Date": "10/23/2018",
        "Vendor": "Uno Dos Tacos"
    },
    "w_05dc8aaf3180c20619094016d4bdfd64a933f2a6.jpg": {
        "Filename": "w_05dc8aaf3180c20619094016d4bdfd64a933f2a6.jpg",
        "Total $ amount": "53.24",
        "Date": "01/04/2019",
        "Vendor": "Taco Guapo"
    },
    "w_1023f6f5c9df6b3c6a77c231d17d4402f7321bb4.pdf": {
        "Filename": "w_1023f6f5c9df6b3c6a77c231d17d4402f7321bb4.pdf",
        "Total $ amount": "50.49",
        "Date": "01/31/2019",
        "Vendor": "Uber"
    },
    "w_20f776a14fa6e002022f53d03d3f5aa85a39ca6f.pdf": {
        "Filename": "w_20f776a14fa6e002022f53d03d3f5aa85a39ca6f.pdf",
        "Total $ amount": "52.45",
        "Date": "12/05/2018",
        "Vendor": "Uber"
    },
    "w_127ced561a4a4e8e3cba7acb656d27544bd06c9c.jpg": {
        "Filename": "w_127ced561a4a4e8e3cba7acb656d27544bd06c9c.jpg",
        "Total $ amount": "9.05",
        "Date": "05/30/2019",
        "Vendor": "Uno Dos Tacos"
    },
    "w_14e2575d8ba3493d2dbc7877e7f2f5c62982a11e.jpg": {
        "Filename": "w_14e2575d8ba3493d2dbc7877e7f2f5c62982a11e.jpg",
        "Total $ amount": "15.58",
        "Date": "05/06/2019",
        "Vendor": "Uber"
    },
    "w_0dad00f35b995d449de524d7f176b403593cc7bb.jpg": {
        "Filename": "w_0dad00f35b995d449de524d7f176b403593cc7bb.jpg",
        "Total $ amount": "24.5",
        "Date": "12/04/2019",
        "Vendor": "Uber"
    }
}



def custom_greeting(name: Text, **kwargs: Any) -> Text:
  """
  Builds a greeting for the user, which addresses them by name.

  Args:
    name (str): the name to greet

  Returns:
    A greeting

  Examples:
    custom_greeting('Alex') -> 'Hello, Alex!'
  """
  return "Hello, {}!".format(name)

def custom_find(find_in_text: Text, query: Text, REFINER_FNS: Any,
                **kwargs: Any) -> Text:
  """
  Finds text to the right of a given query string in a text segment.

  Args:
    find_in_text (str): Text within which to search
    query (str): Label to scan right of
    REFINER_FNS (any): Special refiner variable that maps to the set of refiner functions

  Returns:
    Result of scan_right of query in find_in_text
  """
  return REFINER_FNS.call('scan_right', find_in_text, query)

def getDate(input_col,**kwargs):
  ninput_col = input_col
  input_col = re.split('\n+',input_col)
  rgx = re.compile('(\d\d\d\d+\/\d\d\/\d\d)|(\d+-\d\d-\d\d\d\d)|(\d+\/\d\d\/\d\d\d\d)|((?:J(?:u(?:ly?|ne?)|an(?:uary)?)|A(?:ug(?:ust)?|pril)|Sep(?:t(?:ember)?)?|Ma(?:r(?:ch)?|y)|Dec(?:ember)?|Feb(?:ruary)?|Nov(?:ember)?|Oct(?:ober)?)\s+\d+(\s|\,)+\d\d\d\d)|(\d+\s+(?:J(?:u(?:ly?|ne?)|an(?:uary)?)|A(?:ug(?:ust)?|pril)|Sep(?:t(?:ember)?)?|Ma(?:r(?:ch)?|y)|Dec(?:ember)?|Feb(?:ruary)?|Nov(?:ember)?|Oct(?:ober)?)(\,)\s+\d\d\d\d)|(\d+\s+(?:J(?:u(?:ly?|ne?)|an(?:uary)?)|A(?:ug(?:ust)?|pril)|Sep(?:t(?:ember)?)?|Ma(?:r(?:ch)?|y)|Dec(?:ember)?|Feb(?:ruary)?|Nov(?:ember)?|Oct(?:ober)?)\s+\d\d)|(\d+\s*\,\s+(?:J(?:u(?:ly?|ne?)|an(?:uary)?)|A(?:ug(?:ust)?|pril)|Sep(?:t(?:ember)?)?|Ma(?:r(?:ch)?|y)|Dec(?:ember)?|Feb(?:ruary)?|Nov(?:ember)?|Oct(?:ober)?)\s+\d\d\d\d)|(\d+\-(?:J(?:u(?:ly?|ne?)|an(?:uary)?)|A(?:ug(?:ust)?|pril)|Sep(?:t(?:ember)?)?|Ma(?:r(?:ch)?|y)|Dec(?:ember)?|Feb(?:ruary)?|Nov(?:ember)?|Oct(?:ober)?)\-\d\d\d\d)|(\d\d\d\d-\d+-\d\d)|(\d\d\/\d\d\/\d\d)')
  dates = [col for col in input_col if re.search(rgx,col)]
  match = re.split('\s+',dates[0])
  ans = []
  try:
    ans = [val for val in match if re.search(rgx,val)]
  except:
    return "Error"
  return re.match(rgx,ans[0]).group()


def getsecondDate(input_col,**kwargs):
  rgx = re.compile('((?:J(?:u(?:ly?|ne?)|an(?:uary)?)|A(?:ug(?:ust)?|pril)|Sep(?:t(?:ember)?)?|Ma(?:r(?:ch)?|y)|Dec(?:ember)?|Feb(?:ruary)?|Nov(?:ember)?|Oct(?:ober)?)\s+(\d)?\d\,\s+\d\d\d\d)|((\d)?\d\s+(?:J(?:u(?:ly?|ne?)|an(?:uary)?)|A(?:ug(?:ust)?|pril)|Sep(?:t(?:ember)?)?|Ma(?:r(?:ch)?|y)|Dec(?:ember)?|Feb(?:ruary)?|Nov(?:ember)?|Oct(?:ober)?)\,\s*\d\d\d\d)|(\d\d\d\d\s*\,\s*(?:J(?:u(?:ly?|ne?)|an(?:uary)?)|A(?:ug(?:ust)?|pril)|Sep(?:t(?:ember)?)?|Ma(?:r(?:ch)?|y)|Dec(?:ember)?|Feb(?:ruary)?|Nov(?:ember)?|Oct(?:ober)?)\s+(\d)?\d)')
  x = re.findall(rgx,input_col)
  x = x[0]
  x = x[0]
  x = x.replace(',','')
  return x

def getsecondTotal(input_col,**kwargs):
  rgx = re.compile('\$\d+\s+\d\d|\$\d+\.\d\d')
  amounts = re.findall(rgx,input_col)

  Amount = -1.0
  for val in amounts:
    if val!="":
        x = val.replace('$','')
        x = re.split(' ',x)
        if(len(x) > 1):
          z = float(x[0])
          y = float(x[1])
          x = z + (y/100)
        else:
          x = float(x[0])

        Amount = max(Amount,x)
  return Amount

def getTotal(input_col,**kwargs):
  rgx = re.compile('(?:T(?:otal:?|OTAL|L)|Balance\s+Due|SALE\s+AMOUNT|total:?|alance|otal)')
  rgx2 = re.compile('(\d+\.\d\d)|\s\s\s*(\d+\ \d\d)\s\s\s*')
  rgx3 = re.compile('(?:ME\s+OBLIGO\s+EN\s+LOS\s+TERMINOS|I\s*agree\s*to\s+p(a)?y|Thank\s+You)')
  input_col = input_col.replace('$',' ')
  input_col = re.split('\n',input_col)
  marker = -1
  check = []
  marker2 = len(input_col)-1
  for i in range(len(input_col)):
    if re.search(rgx,input_col[i]) and marker==-1:
      marker = i
      check.append(input_col[i])
      break
  amounts = []
  for i in range(marker,marker2+1):
    amounts.extend(re.findall(rgx2,input_col[i]))
  
  answer = -1.0
  for values in amounts:
    for val in values:
      if val!="":
        answer = max(answer,float(val))

  return answer


def getVendor(input_col, marker,REFINER_FNS,**kwargs):
  if marker=='Not available':
    return "Cannot extract Vendor"
  
  rows = re.split('\n',input_col)
  rows = [REFINER_FNS.call('clean',row) for row in rows]
  
  rows = [row[0] for row in rows]
  i=0
  while i<len(rows) and not (marker in rows[i]):
    i=i+1
  selectedRows = rows[0:i]
  selection = [select.replace(' ','') for select in selectedRows]
  j = i-1
  while j>=0:
    if re.search('([0-9])',selection[j]):
      break
    
    if re.search('(\*)+',selection[j]):
      break
    j=j-1
  
  return selectedRows[j+1]
  
def renderFilename(filename,**kwargs):
  filename = re.split('/',filename)
  return filename[len(filename)-1]  

def get_golden_total(filename,**kwargs):
  filename = renderFilename(filename)
  if filename in goldenData.keys():
    return goldenData[filename]["Total $ amount"]
  return "Not available"

def get_golden_vendor(filename,**kwargs):
  filename = renderFilename(filename)
  if filename in goldenData.keys():
    return goldenData[filename]['Vendor']
  return "Not available"


def get_golden_date(filename,**kwargs):
  filename = renderFilename(filename)
  if filename in goldenData.keys():
    return goldenData[filename]["Date"]
  return "Not available"



import re

# from instabase.provenance.tracking import Value

# From USPS https://pe.usps.com/text/pub28/28apc_002.htm
STREET_SUFFIX = [
    "ALLEY", "ALY", "ALLEE", "ALLEY", "ALLY", "ALY", "ANEX", "ANX", "ANEX",
    "ANNEX", "ANNX", "ANX", "ARCADE", "ARC", "ARC", "ARCADE ", "AVENUE", "AVE",
    "AV", "AVE", "AVEN", "AVENU", "AVENUE", "AVN", "AVNUE", "BAYOU", "BYU",
    "BAYOO", "BAYOU", "BYU", "BEACH", "BCH", "BCH", "BEACH", "BEND", "BND",
    "BEND", "BND", "BLUFF", "BLF", "BLF", "BLUF", "BLUFF", "BLUFFS", "BLFS",
    "BLUFFS", "BLFS", "BOTTOM", "BTM", "BOT", "BTM", "BOTTM", "BOTTOM",
    "BOULEVARD", "BLVD", "BIVD", "BOUL", "BOULEVARD", "BOULV", "BOX", "BRANCH",
    "BR", "BR", "BRNCH", "BRANCH", "BRIDGE", "BRG", "BRDGE", "BRG", "BRIDGE",
    "BROOK", "BRK", "BRK", "BROOK", "BROOKS", "BRKS", "BROOKS", "BRKS", "BURG",
    "BG", "BURG", "BG", "BURGS", "BGS", "BURGS", "BGS", "BYPASS", "BYP", "BYP",
    "BYPA", "BYPAS", "BYPASS", "BYPS", "CAMP", "CP", "CAMP", "CP", "CMP",
    "CANYON", "CYN", "CANYN", "CANYON", "CNYN", "CYN", "CAPE", "CPE", "CAPE",
    "CPE", "CAUSEWAY", "CSWY", "CAUSEWAY", "CAUSWA", "CSWY", "CENTER", "CTR",
    "CEN", "CENT", "CENTER", "CENTR", "CENTRE", "CNTER", "CNTR", "CTR",
    "CENTERS", "CTRS", "CENTERS", "CTRS", "CIRCLE", "CIR", "CIR", "CIRC",
    "CIRCL", "CIRCLE", "CRCL", "CRCLE", "CIRCLES", "CIRS", "CIRCLES", "CIRS",
    "CLIFF", "CLF", "CLF", "CLIFF", "CLIFFS", "CLFS", "CLFS", "CLIFFS", "CLUB",
    "CLB", "CLB", "CLUB", "COMMON", "CMN", "COMMON", "CMN", "COMMONS", "CMNS",
    "COMMONS", "CMNS", "CORNER", "COR", "COR", "CORNER", "CORNERS", "CORS",
    "CORNERS", "CORS", "COURSE", "CRSE", "COURSE", "CRSE", "COURT", "CT",
    "COURT", "CT", "COURTS", "CTS", "COURTS", "CTS", "COVE", "CV", "COVE",
    "CV", "COVES", "CVS", "COVES", "CVS", "CREEK", "CRK", "CREEK", "CRK",
    "CRESCENT", "CRES", "CRESCENT", "CRES", "CRSENT", "CRSNT", "CREST", "CRST",
    "CREST", "CRST", "CROSSING", "XING", "CROSSING", "CRSSNG ", "XING    ",
    "XING", "CROSSROAD", "XRD", "CROSSROAD", "XRD", "CROSSROADS", "XRDS",
    "CROSSROADS", "XRDS", "CURVE ", "CURV", "CURVE", "CURV", "DALE", "DL",
    "DALE", "DL", "DL", "DAM", "DM", "DAM", "DM", "DM", "DIVIDE", "DV", "DIV",
    "DIVIDE", "DV", "DVD", "DRIVE", "DR", "DR", "DRIV", "DRIVE", "DRV",
    "DRIVES", "DRS", "DRIVES", "DRS", "ESTATE", "EST", "EST", "ESTATE",
    "ESTATES", "ESTS", "ESTATES", "ESTS", "EXPRESSWAY", "EXPY", "EXP", "EXPR",
    "EXPRESS", "EXPRESSWAY", "EXPW", "EXPY", "EXTENSION", "EXT", "EXT",
    "EXTENSION", "EXTN", "EXTNSN", "EXTENSIONS", "EXTS", "EXTS", "FALL",
    "FALL", "FALL", "FALLS", "FLS", "FALLS", "FLS", "FERRY", "FRY", "FERRY",
    "FRRY", "FRY", "FIELD", "FLD", "FIELD", "FLD", "FIELDS", "FLDS", "FIELDS",
    "FLDS", "FLAT", "FLT", "FLAT", "FLT", "FLATS", "FLTS", "FLATS", "FLTS",
    "FORD", "FRD", "FORD", "FRD", "FORDS", "FRDS", "FORDS", "FRDS", "FOREST",
    "FRST", "FOREST", "FORESTS", "FRST", "FORGE", "FRG", "FORG", "FORGE",
    "FRG", "FORGES", "FRGS", "FORGES", "FRGS", "FORK", "FRK", "FORK", "FRK",
    "FORKS", "FRKS", "FORKS", "FRKS", "FORT", "FT", "FORT", "FRT", "FT",
    "FREEWAY", "FWY", "FREEWAY", "FREEWY", "FRWAY", "FRWY", "FWY", "GARDEN",
    "GDN", "GARDEN", "GARDN", "GRDEN", "GRDN", "GDN", "GARDENS", "GDNS",
    "GARDENS", "GDNS", "GRDNS", "GATEWAY", "GTWY", "GATEWAY", "GATEWY",
    "GATWAY", "GTWAY", "GTWY", "GLEN", "GLN", "GLEN", "GLN", "GLENS", "GLNS",
    "GLENS", "GLNS", "GREEN", "GRN", "GREEN", "GRN", "GREENS", "GRNS",
    "GREENS", "GRNS", "GROVE", "GRV", "GROV", "GROVE", "GRV", "GROVES", "GRVS",
    "GROVES", "GRVS", "HARBOR", "HBR", "HARB", "HARBOR", "HARBR", "HBR",
    "HRBOR", "HARBORS", "HBRS", "HARBORS", "HBRS", "HAVEN", "HVN", "HAVEN",
    "HVN", "HEIGHTS", "HTS", "HT", "HTS", "HIGHWAY", "HWY", "HIGHWAY",
    "HIGHWY", "HIWAY", "HIWY", "HWAY", "HWY", "HILL", "HL", "HILL", "HL",
    "HILLS", "HLS", "HILLS", "HLS", "HOLLOW", "HOLW", "HLLW", "HOLLOW",
    "HOLLOWS", "HOLW", "HOLWS", "INLET", "INLT", "INLT", "ISLAND", "IS", "IS",
    "ISLAND", "ISLND", "ISLANDS", "ISS", "ISLANDS", "ISLNDS", "ISS", "ISLE",
    "ISLE", "ISLE", "ISLES", "JUNCTION", "JCT", "JCT", "JCTION", "JCTN",
    "JUNCTION", "JUNCTN", "JUNCTON", "JUNCTIONS", "JCTS", "JCTNS", "JCTS",
    "JUNCTIONS", "KEY", "KY", "KEY", "KY", "KEYS", "KYS", "KEYS", "KYS",
    "KNOLL", "KNL ", "KNL", "KNOL", "KNOLL", "KNL ", "KNOLLS", "KNLS", "KNLS",
    "KNOLLS", "LAKE", "LK", "LK", "LAKE", "LAKES", "LKS", "LKS", "LAKES",
    "LAND", "LAND", "LAND", "LANDING", "LNDG", "LANDING", "LNDG", "LNDNG",
    "LANE", "LN", "LANE", "LN", "LIGHT", "LGT", "LGT", "LIGHT", "LIGHTS",
    "LGTS", "LIGHTS", "LGTS", "LOAF", "LF", "LF", "LOAF", "LOCK", "LCK", "LCK",
    "LOCK", "LOCKS", "LCKS", "LCKS", "LOCKS", "LODGE", "LDG", "LDG", "LDGE",
    "LODG", "LODGE", "LOOP", "LOOP", "LOOP", "LOOPS", "MALL", "MALL", "MALL",
    "MANOR", "MNR", "MNR", "MANOR", "MANORS", "MNRS", "MANORS", "MNRS",
    "MEADOW", "MDW", "MEADOW", "MDW", "MEADOWS", "MDWS", "MDW", "MDWS",
    "MEADOWS", "MEDOWS", "MEWS", "MEWS", "MEWS", "MILL", "ML", "MILL", "ML",
    "MILLS", "MLS", "MILLS", "MLS", "MISSION", "MSN", "MISSN", "MSSN", "MSN",
    "MOTORWAY", "MTWY", "MOTORWAY", "MTWY", "MOUNT", "MT", "MNT", "MT",
    "MOUNT", "MOUNTAIN", "MTN", "MNTAIN", "MNTN", "MOUNTAIN", "MOUNTIN",
    "MTIN", "MTN", "MOUNTAINS", "MTNS", "MNTNS", "MOUNTAINS", "MTNS", "NECK",
    "NCK", "NCK", "NECK", "ORCHARD", "ORCH", "ORCH", "ORCHARD", "ORCHRD",
    "OVAL", "OVAL", "OVAL", "OVL", "OVERPASS", "OPAS", "OVERPASS", "OPAS",
    "PARK", "PARK", "PARK", "PRK", "PARKS", "PARK", "PARKS", "PARK", "PARKWAY",
    "PKWY", "PARKWAY", "PARKWY", "PKWAY", "PKWY", "PKY", "PARKWAYS", "PKWY",
    "PARKWAYS", "PKWYS", "PKWY", "PASS", "PASS", "PASS", "PASSAGE", "PSGE",
    "PASSAGE", "PSGE", "PATH", "PATH", "PATH", "PATHS", "PIKE", "PIKE", "PIKE",
    "PIKES", "PINE", "PNE ", "PINE", "PNE ", "PINES", "PNES", "PINES", "PNES",
    "PLACE", "PL", "PL", "PLAIN", "PLN", "PLAIN", "PLN", "PLAINS", "PLNS",
    "PLAINS", "PLNS", "PLAZA", "PLZ", "PLAZA", "PLZ", "PLZA", "POINT", "PT",
    "POINT", "PT", "POINTS", "PTS", "POINTS", "PTS", "PORT", "PRT", "PORT",
    "PRT", "PORTS", "PRTS", "PORTS", "PRTS", "PRAIRIE", "PR", "PR", "PRAIRIE",
    "PRR", "RADIAL", "RADL", "RAD", "RADIAL", "RADIEL", "RADL", "RAMP", "RAMP",
    "RAMP", "RANCH", "RNCH", "RANCH", "RANCHES", "RNCH", "RNCHS", "RAPID",
    "RPD", "RAPID", "RPD", "RAPIDS", "RPDS", "RAPIDS", "RPDS", "REST", "RST",
    "REST", "RST", "RIDGE", "RDG", "RDG", "RDGE", "RIDGE", "RIDGES", "RDGS",
    "RDGS", "RIDGES", "RIVER", "RIV", "RIV", "RIVER", "RVR", "RIVR", "ROAD",
    "RD", "RD", "ROAD", "ROADS", "RDS", "ROADS", "RDS", "ROUTE", "RTE",
    "ROUTE", "RTE", "ROW", "ROW", "ROW", "RUE", "RUE", "RUE", "RUN", "RUN",
    "RUN", "SHOAL", "SHL", "SHL", "SHOAL", "SHOALS", "SHLS", "SHLS", "SHOALS",
    "SHORE", "SHR", "SHOAR", "SHORE", "SHR", "SHORES", "SHRS", "SHOARS",
    "SHORES", "SHRS", "SKYWAY", "SKWY", "SKYWAY", "SKWY", "SPRING", "SPG",
    "SPG", "SPNG", "SPRING", "SPRNG", "SPRINGS", "SPGS", "SPGS", "SPNGS",
    "SPRINGS", "SPRNGS", "SPUR", "SPUR", "SPUR", "SPURS", "SPUR", "SPURS",
    "SPUR", "SQUARE", "SQ", "SQ", "SQR", "SQRE", "SQU", "SQUARE", "SQUARES",
    "SQS", "SQRS", "SQUARES", "SQS", "STATION", "STA", "STA", "STATION",
    "STATN", "STN", "STRAVENUE", "STRA", "STRA", "STRAV", "STRAVEN",
    "STRAVENUE", "STRAVN", "STRVN", "STRVNUE", "STREAM", "STRM", "STREAM",
    "STREME", "STRM", "STREET", "ST", "STREET", "STRT", "ST", "STR", "STREETS",
    "STS", "STREETS", "STS", "SUMMIT", "SMT", "SMT", "SUMIT", "SUMITT",
    "SUMMIT", "TERRACE", "TER", "TER", "TERR", "TERRACE", "THROUGHWAY", "TRWY",
    "THROUGHWAY", "TRWY", "TRACE", "TRCE", "TRACE", "TRACES", "TRCE", "TRACK",
    "TRAK", "TRACK", "TRACKS", "TRAK", "TRK", "TRKS", "TRAFFICWAY", "TRFY",
    "TRAFFICWAY", "TRFY", "TRAIL", "TRL", "TRAIL", "TRAILS", "TRL", "TRLS",
    "TRAILER", "TRLR", "TRAILER", "TRLR", "TRLRS", "TUNNEL", "TUNL", "TUNEL",
    "TUNL", "TUNLS", "TUNNEL", "TUNNELS", "TUNNL", "TURNPIKE", "TPKE", "TRNPK",
    "TURNPIKE", "TURNPK", "TPKE", "UNDERPASS", "UPAS", "UNDERPASS", "UPAS",
    "UNION", "UN", "UN", "UNION", "UNIONS", "UNS", "UNIONS", "UNS", "VALLEY",
    "VLY", "VALLEY", "VALLY", "VLLY", "VLY", "VALLEYS", "VLYS", "VALLEYS",
    "VLYS", "VIADUCT", "VIA", "VDCT", "VIA", "VIADCT", "VIADUCT", "VIEW", "VW",
    "VIEW", "VW", "VIEWS", "VWS", "VIEWS", "VWS", "VILLAGE", "VLG", "VILL",
    "VILLAG", "VILLAGE", "VILLG", "VILLIAGE", "VLG", "VILLAGES", "VLGS",
    "VILLAGES", "VLGS", "VILLE", "VL", "VILLE", "VL", "VISTA", "VIS", "VIS",
    "VIST", "VISTA", "VST", "VSTA", "WALK", "WALK", "WALK", "WALKS", "WALK",
    "WALKS", "WALK", "WALL", "WALL", "WALL", "WAY", "WAY", "WY", "WAY", "WAYS",
    "WAYS", "WAYS", "WELL", "WL", "WELL", "WL", "WELLS", "WLS", "WELLS", "WLS"
]
STREET_SECOND_UNIT = [
    "APARTMENT", 'APT', 'BASEMENT', 'BSMT', 'BUILDING', 'BLDF', 'DEPARTMENT',
    'DEPT', 'FLOOR', 'FL', 'FRONT', 'FRNT', 'HANGER', 'HNGR', 'KEY', 'KEY',
    'LOBBY', 'LBBT', 'LOT', 'LOT', 'LOWER', 'LOWR', 'OFFICE', 'OFC',
    'PENTHOUSE', 'PH', 'PIER', 'PIER', 'REAR', 'REAR', 'ROOM', 'RM', 'SIDE',
    'SIDE', 'SLIP', 'SLIP', 'SPACE', 'SPC', 'STOP', 'STOP', 'SUITE', 'STE',
    'TRAILER', 'TRLR', 'UNIT', 'UPPER', 'UPPR', '\#'
]
US_STATES = [
    "ALABAMA", "AL", "ALASKA", "AK", "AMERICAN SAMOA", "AS", "ARIZONA", "AZ",
    "ARKANSAS", "AR", "CALIFORNIA", "CA", "COLORADO", "CO", "CONNECTICUT",
    "CT", "DELAWARE", "DE", "DISTRICT OF COLUMBIA", "DC",
    "FEDERATED STATES OF MICRONESIA", "FM", "FLORIDA", "FL", "GEORGIA", "GA",
    "GUAM", "GU", "HAWAII", "HI", "IDAHO", "ID", "ILLINOIS", "IL", "INDIANA",
    "IN", "IOWA", "IA", "KANSAS", "KS", "KENTUCKY", "KY", "LOUISIANA", "LA",
    "MAINE", "ME", "MARSHALL ISLANDS", "MH", "MARYLAND", "MD", "MASSACHUSETTS",
    "MA", "MICHIGAN", "MI", "ML", "MINNESOTA", "MN", "MISSISSIPPI", "MS",
    "MISSOURI", "MO", "MONTANA", "MT", "NEBRASKA", "NE", "NEVADA", "NV",
    "NEW HAMPSHIRE", "NH", "NEW JERSEY", "NJ", "NEW MEXICO", "NM", "NEW YORK",
    "NY", "NORTH CAROLINA", "NC", "NORTH DAKOTA", "ND",
    "NORTHERN MARIANA ISLANDS", "MP", "OHIO", "OH", "OKLAHOMA", "OK", "OREGON",
    "OR", "PALAU", "PW", "PENNSYLVANIA", "PA", "PUERTO RICO", "PR",
    "RHODE ISLAND", "RI", "RL", "SOUTH CAROLINA", "SC", "SOUTH DAKOTA", "SD",
    "TENNESSEE", "TN", "TEXAS", "TX", "UTAH", "UT", "VERMONT", "VT",
    "VIRGIN ISLANDS", "VI", "VL", "VIRGINIA", "VA", "WASHINGTON", "WA",
    "WEST VIRGINIA", "WV", "WISCONSIN", "WI", "WL", "WYOMING", "WY"
]

US_STATES_REGEX = ('(' + '|'.join(US_STATES) + ')').replace(' ', ' +')
CITY_STATE_ZIP_REGEX = '(( ){0,5})([A-Z\.\-]+(( ){1,25})){0,3}[A-Z\.\-]+ *[\,\.]? *' + US_STATES_REGEX + ' +([\dIl\/SBb\?] {0,2}){5}( *\-?([\dIl\/SBb\?] {0,2}){4})?(( ){1,30}|\n|$)'
STREET_NUM_NAME_REGEX = '([NS]?[\d\?]+(\-[\d\?]+)*|ONE) *(([A-Z0-9\.\/]+ *){1,5})'  # 7 sometimes scanned as ?
STREET_SUFFIX_SECOND_UNIT_REGEX = '(' + (
    '|'.join(STREET_SUFFIX)
) + ')\.?(' + '.*(' + '|'.join(STREET_SECOND_UNIT) + ')' + ' *\.?\#? *\d+)?'
PO_BOX_REGEX = ' *[PR].*O.*[BV]O(X|Kh) *\#? *\d+'  # PO BOX regex with some ocr error tolerence

# above patterns work for addresses separated into multiple lines. the flat pattern works for addresses that are in one line.
STREET_NUM_NAME_FLAT_REGEX = '(^|\n| )([NS]?[\d]+(\-\d+)*|ONE) +([A-Z\.0-9]+ +){1,5}'
STREET_SUFFIX_SECOND_UNIT_FLAT_REGEX = '(' + (
    '|'.join(STREET_SUFFIX)) + ') *\.?(' + '[^a-zA-Z0-9]*(' + '|'.join(
        STREET_SECOND_UNIT) + ')' + ' *\.?\#? *\d+)?[^a-zA-Z0-9]*'
PO_BOX_FLAT_REGEX = ' *P.*O.*BOX +\d+[^a-zA-Z0-9]*'


# make each line in the text to have the same length
def __same_width_text(text, **kwargs):
  maxLength = max(map(lambda x: len(x), text.split('\n')))
  output = []
  for line in text.split('\n'):
    line = line + ' ' * (maxLength - len(line))
    output.append(line)
  return '\n'.join(output)


# def __same_width_text_v(text, **kwargs):
#   try:
#     input_col = text.value()
#     tracker = text.tracker()
#     output = Value(same_width_text(input_col))
#     if tracker:
#       output.set_tracker(tracker)
#     return output
#   except Exception as e:
#     return Value(e)


# Find address and name above the address given text. limit is how many adress/name to search for.
def get_address(text, limit=1, **kwargs):
  name_or_address = 'address'
  skip_state_regex = kwargs.get(
      'skip_state_regex', None
  )  # pattern to skip when finding a CITY-STATE-ZIPCODE pattern - enable skipping certain states
  # if it is possible for a name to be separated into multiple lines/having multiple names (like W2 or bank statements), specify a regex to tell the function when to stop "looking up" after finding an address. by default it stops after getting the first reasonable line above the address.
  name_stop_regex = kwargs.get('name_stop_regex', None)
  # by default the function ignore address that only has CITY-STATE-ZIPCODE but not have a street address. You can specify how many addresses you want to allow just having city-state-zip
  no_street_address_num = kwargs.get('no_street_address_num', None)
  # skip PO Box address
  no_po_box = kwargs.get('no_po_box', None)

  regexState = re.compile(CITY_STATE_ZIP_REGEX, re.I)  # Compile all regex
  if no_po_box is None:
    regexStreet = re.compile(
        '(' + STREET_NUM_NAME_REGEX + STREET_SUFFIX_SECOND_UNIT_REGEX + '|' +
        PO_BOX_REGEX + ')', re.I)
  else:
    regexStreet = re.compile(
        STREET_NUM_NAME_REGEX + STREET_SUFFIX_SECOND_UNIT_REGEX, re.I)
  regexStreetSecondLine = re.compile(
      '^ *(' + '|'.join(STREET_SECOND_UNIT) + ')' + ' *\.? *\d+', re.I)

  if no_po_box is None:
    regexStreetFlat = re.compile(
        '(' + STREET_NUM_NAME_FLAT_REGEX + STREET_SUFFIX_SECOND_UNIT_FLAT_REGEX
        + '|' + PO_BOX_FLAT_REGEX + ')' + CITY_STATE_ZIP_REGEX, re.I)
  else:
    regexStreetFlat = re.compile(
        STREET_NUM_NAME_FLAT_REGEX + STREET_SUFFIX_SECOND_UNIT_FLAT_REGEX +
        CITY_STATE_ZIP_REGEX, re.I)

  text = __same_width_text(text)  # make text the same length
  lineLength = text.find('\n') + 1 if text.find('\n') > -1 else len(text)
  result = []

  for match in re.finditer(
      regexState, text):  # find all CITY-STATE-ZIPCODE pattern in text
    if re.search('(employee|employer|group) *id', match.group(0),
                 re.I) is not None:  # ID is Idaho :) Skip those
      continue
    if skip_state_regex is not None and re.search(
        skip_state_regex, match.group(0), re.I) is not None:
      continue

    city_state_zip = match.group(0)
    startI = match.start(0)
    endI = match.end(0)
    line = int(startI / lineLength)
    startCol = int(startI % lineLength)
    stringLength = int(endI - startI)

    startCol_adjust = 0  # might need to adjust the start col later - we don't know when is the start of a city name. will adjust using stree number location later

    # first, check if it's a one-line address
    currentLine = text[
        line * lineLength:
        endI]  # grab the line from start to the end of CITY-STATE-ZIP
    matchFlatAddress = re.search(regexStreetFlat, currentLine)
    if matchFlatAddress is not None:
      if name_or_address == 'address':
        address = re.sub(' +', ' ', matchFlatAddress.group(0).strip())
        if address not in result:
          result.append(address)
      else:
        s = currentLine[:matchFlatAddress.start(
            0)]  # name could be before the address in the smae line
        s = re.sub(' +', ' ', s.strip())
        if len(
            s
        ) == 0 and line > 0:  # if in front of the address there's nothing... find the line above
          s = text[(line - 1) * lineLength +
                   int(matchFlatAddress.start(0) % lineLength):
                   (line - 1) * lineLength + startCol + stringLength]
          s = re.sub(' +', ' ', s.strip())
        if len(s) > 0 and s not in result:
          result.append(s)
      if len(result) >= limit:
        return result
    else:  # for multi-line address, check lines above the CITY STATE line
      if name_or_address == 'address':
        address = city_state_zip
      else:
        current_name_out = ''
      had_street_address = False
      for l in range(line - 1, max(line - 15, -1),
                     -1):  # look for at most 15 lines
        # don't cut text from the middle of a word
        temp_start_col = startCol
        while temp_start_col > 0:
          if text[l * lineLength + temp_start_col - 1:l * lineLength +
                  temp_start_col] != ' ':
            temp_start_col -= 1
          else:
            break
        temp_end_col = startCol + stringLength
        while temp_end_col < lineLength:
          if text[l * lineLength + temp_end_col:l * lineLength + temp_end_col +
                  1] != ' ' and text[l * lineLength + temp_end_col:l *
                                     lineLength + temp_end_col + 1] != '\n':
            temp_end_col += 1
          else:
            break
        fullString = text[l * lineLength + temp_start_col:min(
            l * lineLength + temp_end_col, len(text)
        )]  # string above `CITY-STATE-ZIP` with some paddings left n right
        if name_or_address == 'name' and len(
            current_name_out) > 0 and re.search(name_stop_regex, fullString,
                                                re.I) is not None:
          if current_name_out not in result:
            result.append(current_name_out)
            if len(result) >= limit:
              return result
          break

        s = fullString.strip()
        if re.search('\s{20}', s) is not None:
          s = s[:re.search('\s{20}', s).start(
              0)]  # cut out words that are 20 spaces apart
        s = s.replace(' ', '')  # remove all spaces

        s_above = ''  # text above the current line
        if l - 1 > max(line - 15, -1):
          s_above = re.sub(
              '[^A-Za-z]', '', text[(l - 1) * lineLength + temp_start_col:min(
                  (l - 1) * lineLength + temp_end_col, len(text))])
        # sometimes there is only CITY, STATE and there's no actual street address. Ignore those and only look at things that have a street address
        if len(s) > 0 and re.search(regexStreetSecondLine, s) is not None:
          if name_or_address == 'address':
            address = fullString + '\n' + address
        elif len(s) > 0 and (
            re.search(regexStreet, s) is not None or
            (l == line - 1 and re.search(
                '(\d+(\-\d+)*|ONE)[A-Z]{3}|\d+[WENS]\d+[WENS]', s) is not None)
        ):  # if found a street adress or a street num + street name directly above the state name line
          had_street_address = True
          if name_or_address == 'address':
            address = fullString + '\n' + address
            address = re.sub(' +', ' ', address.strip())
            if address not in result:
              result.append(address)
              if len(result) >= limit:
                return result
            break
          elif re.search(
              'P.*O.*|(\d+(\-\d+)*|ONE)', fullString, re.I
          ) is not None:  # modify start col based on start of the street regex
            startCol_adjust = re.search(
                'P.*O.*|(\d+(\-\d+)*|ONE)', fullString,
                re.I).start(0) - (startCol - temp_start_col)
            startCol += startCol_adjust
            stringLength -= startCol_adjust
        elif not had_street_address and no_street_address_num is not None and len(
            re.sub('[^A-Za-z]', '', s)
        ) > 10 and len(result) < int(
            no_street_address_num
        ):  # at least 10 characters and is the first possible address? (usually employer name)
          had_street_address = True  # alright, this could be an address
          if name_or_address == 'address':
            address = re.sub(' +', ' ', address.strip())
            if address not in result:
              result.append(address)
              if len(result) >= limit:
                return result
            break
        elif had_street_address and re.search(
            r'[A-Za-z]{2}', s) is not None and re.search(
                regexStreet, s) is None and re.search(regexStreetSecondLine,
                                                      s) is None and re.search(
                                                          r'\d{4}', s) is None:
          if re.search(
              '(address|date|number|employe|title|name|total|amount|hourly|complete|\:|statement|earning)',
              s, re.I
          ) is not None:  # found a title text... skip it and reset startCol
            startCol -= startCol_adjust
            stringLength += startCol_adjust
            startCol_adjust = 0
          elif re.search(
              '(payroll|center|board|attn)', s, re.I) is not None and len(
                  s_above) > 4:  # found a possible second line, skip
            continue
          elif len(re.sub('[^A-Za-z]', '', s)) > 4:  # at least 4 characters?
            # got a name
            # cut out words that are 20 spaces apart
            fullString = fullString.strip()
            if re.search('\s{20}', fullString) is not None:
              fullString = fullString[:re.search('\s{20}', fullString).
                                      start(0)]
            s = re.sub(' +', ' ', fullString)
            if name_stop_regex is None:
              if s not in result:
                result.append(s)
                if len(result) >= limit:
                  return result
              break
            else:
              current_name_out = s + '\n' + current_name_out

  return result




def register(name_to_fn: Any) -> None:
  more_fns = {
      'custom_greeting': {
          'fn': custom_greeting,
          'ex': '',
          'desc': ''
      },
      'custom_find': {
          'fn': custom_find,
          'ex': '',
          'desc': ''
      },
      'getdate':{
        'fn':getDate,
        'ex':'',
        'desc':''
      },
      'gettotal':{
        'fn':getTotal,
        'ex':'',
        'desc':''
      },
      'getsecondtotal':{
        'fn':getsecondTotal,
        'ex':'',
        'desc':''
      },
      'get_golden_total':{
        'fn':get_golden_total,
        'ex':'',
        'desc':''
      },
      'get_golden_vendor':{
        'fn':get_golden_vendor,
        'ex':'',
        'desc':''
      },
      'get_golden_date':{
        'fn':get_golden_date,
        'ex':'',
        'desc':''
      },
      'get_address':{
        'fn':get_address,
        'ex':'',
        'desc':''
      },
      'get_vendor':{
        'fn':getVendor,
        'ex':'',
        'desc':''
      },
      'get_seconddate':{
        'fn':getsecondDate,
        'ex':'',
        'desc':''
      }
  }
  name_to_fn.update(more_fns)
