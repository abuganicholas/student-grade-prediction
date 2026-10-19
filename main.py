
import pandas as pd

data= {
    "student":["Alice","Brian","Carol","David","Esther"],
    "study hours":[2,4,3,6,5],
    "exam score":[50,65,58,85,78]
}

df=pd.DataFrame(data)

print(df)

mean_score = df["exam score"].mean()

print("\n mean exam score is",mean_score)

median_score=df["exam score"].median()

print("\n median exam score is",median_score)

mode_score=df["exam score"].mode()

print("\n mode exam score is",mode_score)

highest_score=df["exam score"].max()

lowest_score=df["exam score"].min()

score_range= highest_score-lowest_score

print("\n highest exam score is",highest_score)
print("\n lowest exam score is",lowest_score)
print("\n Range of exam scores:",score_range)

std_score=df["exam score"].std()

print("\n Standard deviation of exam scores:",f"{std_score:.2f}")

correlation = df["study hours"].corr(df["exam score"])

print("\n Correlation btn study hours and exam scores:",correlation)



from sklearn.linear_model import LinearRegression

X = df[["study hours"]]
y = df["exam score"]

#creating model 1
model = LinearRegression()

#Train the model
model.fit(X, y)
predictions = model.predict(X)

print("\n Actual scores:",list(y))
print("\n Predicted scores:",predictions.round(2))

#predicting scores for the regression
line_scores = model.predict(X)

import matplotlib.pyplot as pit

#drawing the regression line
pit.plot(df["study hours"], line_scores)

predicted_score = model.predict(
    pd.DataFrame({"study hours": [5]})
)
print("\n Prediction for 5 study hours:",predicted_score)


pit.scatter(df["study hours"],df["exam score"])

pit.title("exam score vs study hours")
pit.xlabel("study hours")
pit.ylabel("exam score")

#Draw the regression line
line_scores = model.predict(X)
pit.plot(df["study hours"], line_scores)


pit.savefig("images/study_hours_vs_scores.png")
pit.show()

from sklearn.metrics import mean_absolute_error

MAD = mean_absolute_error(y, predictions)

print("\n Mean Absolute Error:"f"{MAD:.2f}")

from sklearn.metrics import r2_score

r2 = r2_score(y, predictions)

print("\n R-squared score:", round(r2, 3))

print("\n--- MODEL PERFORMANCE ---")
print("Mean Absolute Error:",f"{MAD:.2f}")
print("R-squared score:", round(r2, 3))
print("Prediction for 5 study hours:",
      round(model.predict(
          pd.DataFrame({"study hours": [5]})
      )[0], 2))


