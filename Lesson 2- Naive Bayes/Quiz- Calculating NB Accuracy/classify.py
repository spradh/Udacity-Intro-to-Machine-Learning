def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()#TODO

    ### fit the classifier on the training features and labels
    #TODO
    clf.fit(features_train, labels_train)
    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_train)#TODO


    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(labels_train,pred)#TODO
    return accuracy
