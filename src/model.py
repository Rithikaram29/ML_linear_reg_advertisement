from .train import train_model

def model_prediction(x_train,y_train,x_test):
    trained_model = train_model(x_train,y_train)
    predictions = trained_model.predict(x_test)
    # print(predictions)
    return predictions
    
    