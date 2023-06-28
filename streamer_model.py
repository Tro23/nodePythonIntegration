#Creating the Dataframe

import random

writer = [random.randint(0,24) for x in range(5000)]
executive_producer = [random.randint(0,24) for x in range(5000)]
budget = [random.randint(0,7) for x in range(5000)]
diversity = [random.randint(0,9) for x in range(5000)]
genre = [random.randint(0,8) for x in range(5000)]
story = [random.randint(0,6) for x in range(5000)]
lead_character = [random.randint(0,5) for x in range(5000)]
second_lead = [random.randint(0,4) for x in range(5000)]
locations = [random.randint(0,3) for x in range(5000)]
tone = [random.randint(0,2) for x in range(5000)]
ratings = [random.randint(0,5) for x in range(5000)]
executive_10years = [random.randint(0,3) for x in range(5000)]

import pandas as pd
import numpy as np

success_rate = pd.DataFrame(np.column_stack([writer,
                                                executive_producer,
                                                budget,
                                                diversity,
                                                genre,
                                                story,
                                                lead_character,
                                                second_lead,
                                                tone,
                                                ratings,
                                                executive_10years,]), 
                               columns=['writer',
                                        'executive_producer',
                                        'budget',
                                        'diversity',
                                        'genre',
                                        'story',
                                        'lead_character',
                                        'second_lead',
                                        'tone',
                                        'ratings',
                                        'executive_10years'])

success_rate["Total_Points"] = success_rate.apply(lambda row: sum(row), axis=1)

#Binary Classification

X = success_rate[['writer',
         'executive_producer',
         'budget',
         'diversity',
         'genre',
         'story',
         'lead_character',
         'second_lead',
         'tone',
         'ratings',
         'executive_10years']].to_numpy()

T = success_rate.Total_Points.to_numpy().reshape(-1,1)

from sklearn.model_selection import train_test_split
# train-test split for model evaluation
Xtrain, Xtest, Ttrain, Ttest = train_test_split(X, T, train_size=0.8, shuffle=True)

import torch

n_inputs = X.shape[1]

nHiddens = 10

learning_rate = 0.01

Xt = torch.from_numpy(Xtrain).float()
Tt = torch.from_numpy(Ttrain).float()

Xtestt = torch.from_numpy(Xtest).float()
Ttestt = torch.from_numpy(Ttest).float()

nSteps = 5000
errorTrace = np.zeros((nSteps, 2))

nnet = torch.nn.Sequential(torch.nn.Linear(n_inputs, 10), torch.nn.ReLU(), 
                           torch.nn.Linear(10, 20), torch.nn.ReLU(), 
                           torch.nn.Linear(20, 10), torch.nn.ReLU(), 
                           torch.nn.Linear(10, 1))



mse_f = torch.nn.MSELoss()
optimizer = torch.optim.Adam(nnet.parameters(), lr=learning_rate)

for step in range(nSteps):

    #forward_pass
    Y = nnet(Xt)


    mse = mse_f(Y, Tt)
    
    # Backward pass - the backpropagation and weight update steps
    
    optimizer.zero_grad()
    mse.backward()
    optimizer.step()
    
    # error traces for plotting
    errorTrace[step, 0] = mse.sqrt()
    
    Ytest = nnet(Xtestt)
    mse_test = mse_f(Ytest, Ttestt)
    # Ytest = addOnes(np.tanh(Xtest1 @ V)) @ W  #!! Forward pass in one line
    errorTrace[step, 1] = mse_test.sqrt()


print ('The percentage of Success is', nnet(Xtestt[0]).detach().numpy()[0], ' %')