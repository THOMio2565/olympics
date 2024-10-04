from olympics import db


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 100

def test_select_country():
    rows = db.get_countries(52)
    assert len(rows) == 1

def test_athletes():
    rows = db.get_athletes()
    assert len(rows) > 1000

def test_select_athlete():
    rows = db.get_athletes(76)
    assert len(rows) == 1

def test_disciplines():
    rows = db.get_disciplines()
    assert len(rows) > 10

def test_select_discipline():
    rows = db.get_disciplines(3)
    assert len(rows) == 1

def test_teams():
    rows = db.get_teams()
    assert len(rows) > 100

def test_select_team():
    rows = db.get_teams(2)
    assert len(rows) == 1

def test_events():
    rows = db.get_events()
    assert len(rows) > 100

def test_select_event():
    rows = db.get_events(5)
    assert len(rows) == 1

def test_medals():
    rows = db.get_medals()
    assert len(rows) > 100

def test_select_medal():
    rows = db.get_medals(7)
    assert len(rows) == 1

def test_get_discipline_athletes():
    rows = db.get_discipline_athletes(3)
    assert len(rows) > 3

def test_get_top_countries():
    rows = db.get_top_countries(10)
    assert len(rows) == 10

def test_get_collective_medals():
    rows = db.get_collective_medals()
    assert len(rows) > 0

def test_get_top_collective():
    rows = db.get_top_collective(10)
    assert len(rows) == 10

def test_get_individual_medals():
    rows = db.get_individual_medals()
    assert len(rows) > 100

def test_get_specific_individual_medals():
    rows = db.get_individual_medals(4253)
    assert len(rows) == 2

def test_get_top_individual():
    rows = db.get_top_individual(69)
    assert len(rows) == 69
