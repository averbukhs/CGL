def test_cases(number):
    return testCases[number]

    
testCases = [
    #[severity, description]
    ['Blocker', 'When user goes to main page, page should be loaded'],
    ['Blocker', 'All companies should be presented on the home page'],
    ['Blocker', 'When user filter company name for app it should return only Apple company'],
    ['Blocker', 'When user filter industry by technology it should return only technology companies'],
    ['Blocker', 'When user sort companies by name Apple should be the first one'],
]