import cleanup


def test_remove_euro():
    assert '' == cleanup._remove_euro('€')


def test_remove_whitespace():
    assert '123000' == cleanup._trim_whitespace('123 000')


def test_remove_whitespace_2():
    assert '-€' == cleanup._trim_whitespace(' -  €')


def test_symbol_removal():
    """If field contains just - and € characters, then return empty string."""
    assert '' == cleanup._symbol_removal('-€')


def test_clean_row1():
    assert 'Nokia Oyj;0112038-9;1997;8471160;tutkimus- ja kehitystuki;Tekes;Uusimaa;;2630;Viestintälaitteiden valmistus;NACE;'\
        == cleanup.clean_line('Nokia Oyj;0112038-9;1997; 8 471 160 € ;tutkimus- ja kehitystuki;Tekes;Uusimaa;;2630;Viestintälaitteiden valmistus;NACE;')


def test_clean_row2():
    assert 'PMC Polarteknik Oy Ab;0108305-5;1997;;tutkimus- ja kehitystuki;Tekes;Päijät-Häme;32797;4669;Teollisuudessa käytettävien muiden koneiden tukkukauppa;NACE;'\
        == cleanup.clean_line('PMC Polarteknik Oy Ab;0108305-5;1997; -    €;tutkimus- ja kehitystuki;Tekes;Päijät-Häme; 32 797 € ;4669;Teollisuudessa käytettävien muiden koneiden tukkukauppa;NACE;')


def test_clean_row3():
    assert '"Confiture Printing Studio Oy/\""Painoakat\""";1645657-1;2001;2389;palkkatuki;TE-keskus/TEM;Uusimaa;;13;ei_saatavilla;2008;'\
        == cleanup.clean_line('"Confiture Printing Studio Oy/""Painoakat""";1645657-1;2001; 2 389 € ;palkkatuki;TE-keskus/TEM;Uusimaa;;13;ei_saatavilla;2008;')


def test_clean_row4():
    assert  'Volvo Bus Finland Oy;0153771-5;1997;29892;tutkimus- ja kehitystuki;Tekes;Varsinais-Suomi;;2920;"Moottoriajoneuvojen korien valmistus; perävaunujen ja puoliperävaunujen valmistus";NACE;'\
        == cleanup.clean_line('Volvo Bus Finland Oy;0153771-5;1997;29 892 €;tutkimus- ja kehitystuki;Tekes;Varsinais-Suomi;;2920;"Moottoriajoneuvojen korien valmistus; perävaunujen ja puoliperävaunujen valmistus";NACE;')


def test_clean_row5():
    assert 'Jartek Oy(0717519-6);0717519-6;2000;6939;tutkimus- ja kehitystuki;Tekes;Päijät-Häme;;ei_saatavilla;ei_saatavilla;NACE;'\
        == cleanup.clean_line('Jartek Oy(0717519-6);0717519-6;2000; 6 939 € ;tutkimus- ja kehitystuki;Tekes;Päijät-Häme; -   € ;ei_saatavilla;ei_saatavilla;NACE;')


def test_clean_row6():
    assert '"Commit; Oy";0782881-2;2001;;tutkimus- ja kehitystuki;Tekes;Uusimaa;33638;6201;Ohjelmistojen suunnittelu ja valmistus;NACE;'\
        == cleanup.clean_line('"Commit; Oy";0782881-2;2001; -   € ;tutkimus- ja kehitystuki;Tekes;Uusimaa; 33 638 € ;6201;Ohjelmistojen suunnittelu ja valmistus;NACE;')


def test_clean_row7():
    assert 'Kymenlaakson Jäte Oy;1093000-9;2013;437500;energiatuki/investoinnit;Ely-keskus/TEM;Ei_saatavilla;;38;"Jätteen keruu, käsittely ja loppusijoitus; materiaalien kierrätys";2008;"Kaakkois-Suomen Ely-keskus kattaa usemmman maakunnan; ei määritelty"'\
        == cleanup.clean_line('Kymenlaakson Jäte Oy;1093000-9;2013; 437 500 € ;energiatuki/investoinnit;Ely-keskus/TEM;Ei_saatavilla;;38;"Jätteen keruu, käsittely ja loppusijoitus; materiaalien kierrätys";2008;"Kaakkois-Suomen Ely-keskus kattaa usemmman maakunnan; ei määritelty"')
