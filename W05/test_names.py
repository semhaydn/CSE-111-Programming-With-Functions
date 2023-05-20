from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest



def test_make_full_name():
    # Call the make_full_name function ten times and use an assert
    # statement to verify that the string returned by the
    # make_full_name function is correct each time.

    assert make_full_name("Semih", "Aydin") == "Aydin; Semih"
    assert make_full_name("", "Aydin") == "Aydin; "
    assert make_full_name("Semih", "") == "; Semih"
    assert make_full_name("", "") == "; "
    assert make_full_name("Senanur", "Aydin") == "Aydin; Senanur"
    assert make_full_name("Kemal", "Ataturk") == "Ataturk; Kemal"
    assert make_full_name("Elmas", "Aydin") == "Aydin; Elmas"
    assert make_full_name("Seyfettin", "Koz") == "Koz; Seyfettin"
    assert make_full_name("Ayse", "Aksakal") == "Aksakal; Ayse"
    assert make_full_name("Suat", "Aydin") == "Aydin; Suat"


def test_extract_family_name():
    # Call the test_extract_family_name function ten times and use an assert
    # statement to verify that the string returned by the
    # test_extract_family_name function is correct each time.
    assert extract_family_name("Aydin; Semih") == "Aydin"
    assert extract_family_name("; ") == ""
    assert extract_family_name("; Semih") == ""
    assert extract_family_name("Aydin; ") == "Aydin"

def test_extract_given_name():
    # Call the test_extract_given_name function ten times and use an assert
    # statement to verify that the string returned by the
    # test_extract_given_name function is correct each time.
    assert extract_given_name("Aydin; Semih") == "Semih"
    assert extract_given_name("; ") == ""
    assert extract_given_name("; Semih") == "Semih"
    assert extract_given_name("Aydin; ") == ""


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
