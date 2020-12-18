# Tripped Me Up

Things that stumped me for a bit.

1. The Diigo API doesn't returns an empty JSON object `[]` when it doesn't have more results to give, not a 404 or etc.
1. To terminate the query to the Diigo API I needed to do something like 
```python
if response.json() == "[]":
    break
```
But this doesn't work. You need to literally compare an empty object:
```python
if response.json() == []:
    break
```