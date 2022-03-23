import streamlit as aaast
import pickle
aaamodel = pickle.load(open('RF_price_predicting_model.pkl','rb'))


def main():
    aaast.title("Selling Price Predictor 🚗")
    aaast.markdown("##### Are you planning to sell your car !?\n##### So let's try evaluating the price.. 🤖 ")

  

    aaast.write('')
    aaast.write('')

    aaayears = aaast.number_input('In which year car was purchased ?',1990, 2020, step=1, key ='year')
    aaaYears_old = 2022-aaayears

    aaaPresent_Price = aaast.number_input('What is the current ex-showroom price of the car ?  (In ₹lakhs)', 0.00, 50.00, step=0.5, key ='present_price') 

    aaaKms_Driven = aaast.number_input('What is distance completed by the car in Kilometers ?', 0.00, 500000.00, step=500.00, key ='drived')

    aaaOwner = aaast.radio("The number of owners the car had previously ?", (0, 1, 3), key='owner')

    aaaFuel_Type_Petrol = aaast.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'CNG'), key='fuel')
    if(aaaFuel_Type_Petrol=='Petrol'):
        aaaFuel_Type_Petrol=1
        aaaFuel_Type_Diesel=0
    elif(aaaFuel_Type_Petrol=='Diesel'):
        aaaFuel_Type_Petrol=0
        aaaFuel_Type_Diesel=1
    else:
        aaaFuel_Type_Petrol=0
        aaaFuel_Type_Diesel=0

    aaaSeller_Type_Individual = aaast.selectbox('Are you a dealer or an individual ?', ('Dealer','Individual'), key='dealer')
    if(aaaSeller_Type_Individual=='Individual'):
        aaaSeller_Type_Individual=1
    else:
        aaaSeller_Type_Individual=0	

    aaaTransmission_Mannual = aaast.selectbox('What is the Transmission Type ?', ('Manual','Automatic'), key='manual')
    if(aaaTransmission_Mannual=='Mannual'):
        aaaTransmission_Mannual=1
    else:
        aaaTransmission_Mannual=0


    if aaast.button("Estimate Price", key='predict'):
        try:
            aaaModel = aaamodel  #get_model()
            aaaprediction = aaaModel.predict([[aaaPresent_Price, aaaKms_Driven, vOwner, aaaYears_old, aaaFuel_Type_Diesel, aaaFuel_Type_Petrol, aaaSeller_Type_Individual, aaaTransmission_Mannual]])
            aaaoutput = round(prediction[0],2)
            if aaaoutput<0:
                aaast.warning("You will be not able to sell this car !!")
            else:
                aaast.success("You can sell the car for {} lakhs 🙌".format(aaaoutput))
        except:
            aaast.warning("Opps!! Something went wrong\nTry again")
            



if __name__ == "__main__":
    main()
