from pyModeS import bds, modes

def test_ehs_icao():
    assert modes.icao("A0001839CA3800315800007448D9") == '400940'
    assert modes.icao("A000139381951536E024D4CCF6B5") == '3C4DD2'
    assert modes.icao("A000029CFFBAA11E2004727281F1") == '4243D0'


def test_modes_altcode():
    assert modes.altcode("A02014B400000000000000F9D514") == 32300

def test_modes_idcode():
    assert modes.idcode("A800292DFFBBA9383FFCEB903D01") == '1346'


def test_bds_infer():
    assert bds.infer("A0001838201584F23468207CDFA5") == 'BDS20'
    assert bds.infer("A0001839CA3800315800007448D9") == 'BDS40'
    assert bds.infer("A000139381951536E024D4CCF6B5") == 'BDS50'
    assert bds.infer("A00004128F39F91A7E27C46ADC21") == 'BDS60'

def test_bds_is50or60():
    assert bds.is50or60("A0001838201584F23468207CDFA5", 0, 0, 0) == None
    assert bds.is50or60("A0000000FFDA9517000464000000", 182, 237, 1250) == 'BDS50'
    assert bds.is50or60("A0000000919A5927E23444000000", 413, 54, 18700) == 'BDS60'

def test_els_BDS20_callsign():
    assert bds.bds20.callsign("A000083E202CC371C31DE0AA1CCF") == 'KLM1017_'
    assert bds.bds20.callsign("A0001993202422F2E37CE038738E") == 'IBK2873_'

def test_ehs_BDS40_functions():
    assert bds.bds40.alt40mcp("A000029C85E42F313000007047D3") == 3008
    assert bds.bds40.alt40fms("A000029C85E42F313000007047D3") == 3008
    assert bds.bds40.p40baro("A000029C85E42F313000007047D3") == 1020.0

def test_ehs_BDS50_functions():
    assert bds.bds50.roll50("A000139381951536E024D4CCF6B5") == 2.1
    assert bds.bds50.roll50("A0001691FFD263377FFCE02B2BF9") == -0.4     # signed value
    assert bds.bds50.trk50("A000139381951536E024D4CCF6B5") == 114.258
    assert bds.bds50.gs50("A000139381951536E024D4CCF6B5") == 438
    assert bds.bds50.rtrk50("A000139381951536E024D4CCF6B5") == 0.125
    assert bds.bds50.tas50("A000139381951536E024D4CCF6B5") == 424

def test_ehs_BDS60_functions():
    assert bds.bds60.hdg60("A00004128F39F91A7E27C46ADC21") == 42.715
    assert bds.bds60.ias60("A00004128F39F91A7E27C46ADC21") == 252
    assert bds.bds60.mach60("A00004128F39F91A7E27C46ADC21") == 0.42
    assert bds.bds60.vr60baro("A00004128F39F91A7E27C46ADC21") == -1920
    assert bds.bds60.vr60ins("A00004128F39F91A7E27C46ADC21") == -1920

def test_graycode_to_altitude():
    assert modes.gray2alt('00000000010') == -1000
    assert modes.gray2alt('00000001010') == -500
    assert modes.gray2alt('00000011011') == -100
    assert modes.gray2alt('00000011010') == 0
    assert modes.gray2alt('00000011110') == 100
    assert modes.gray2alt('00000010011') == 600
    assert modes.gray2alt('00000110010') == 1000
    assert modes.gray2alt('00001001001') == 5800
    assert modes.gray2alt('00011100100') == 10300
    assert modes.gray2alt('01100011010') == 32000
    assert modes.gray2alt('01110000100') == 46300
    assert modes.gray2alt('01010101100') == 50200
    assert modes.gray2alt('11011110100') == 73200
    assert modes.gray2alt('10000000011') == 126600
    assert modes.gray2alt('10000000001') == 126700