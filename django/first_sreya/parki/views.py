from django.shortcuts import render
from joblib import load
model = load('./saved model/classifier.joblib')

def predictor(request):
    if request.method == 'POST':
        gender = int(request.POST['gender'])
        PPE = float(request.POST['PPE'])
        DFA = float(request.POST['DFA'])
        RPDE = float(request.POST['RPDE'])
        numPulses = int(request.POST['numPulses'])
        numPeriodsPulses = int(request.POST['numPeriodsPulses'])
        meanPeriodPulses = float(request.POST['meanPeriodPulses'])
        stdDevPeriodPulses = float(request.POST['stdDevPeriodPulses'])
        tqwt_kurtosisValue_dec_35 = float(request.POST['tqwt_kurtosisValue_dec_35'])
        tqwt_kurtosisValue_dec_36 = float(request.POST['tqwt_kurtosisValue_dec_36'])

        # Print the field values in the terminal
        print("Gender:", gender)
        print("PPE:", PPE)
        print("DFA:", DFA)
        print("RPDE:", RPDE)
        print("numPulses:", numPulses)
        print("numPeriodsPulses:", numPeriodsPulses)
        print("meanPeriodPulses:", meanPeriodPulses)
        print("stdDevPeriodPulses:", stdDevPeriodPulses)
        print("tqwt_kurtosisValue_dec_35:", tqwt_kurtosisValue_dec_35)
        print("tqwt_kurtosisValue_dec_36:", tqwt_kurtosisValue_dec_36)

        pred = model.predict([[gender, PPE, DFA, RPDE, numPulses, numPeriodsPulses, meanPeriodPulses, stdDevPeriodPulses, tqwt_kurtosisValue_dec_35, tqwt_kurtosisValue_dec_36]])
        # Assuming the model expects a 2D array input

        verdict = 'Parkinson Detected' if pred == 0 else 'No Issue'


        return render(request, 'main.html', {'verdict': verdict})
    return render(request, 'main.html')
