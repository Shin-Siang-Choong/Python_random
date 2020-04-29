with open('abc.pkl', 'wb') as f:
    pickle.dump(abc, f, -1)
    
abc = pickle.load( open( "abc.pkl", "rb" ) )
