from olympics.__main__ import main


def test_countries():
    argv = ['countries']
    main(argv)

def test_collective():
    argv = ['collective']
    main(argv)

def test_individual():
    argv = ['individual']
    main(argv)

