# BlackCardCounter.package.cardpack.carddata

## Class Card

카드를 만들기 위해 사용


### 카드 만들기
parameters :
- int cardnumber
- string cardshape
- [optional string JQK]
return type : Card Object 
<br>

```
card = Card(int : cardnumber, string : cardshape, [string : JQK = JorQorK])
```


### 카드의 숫자 반환하기
일반적인 카드와 J,Q,K 의 경우, [number] 로 반환됨. <br>
'A' 와 같은 카드의 경우, [1, 11] 으로 반환됨. <br>
parameters : None
return type : list
<br>

```
card_num = card.cardnumber()
```

### 카드의 문자 반환하기
parameters : None
return type : string
<br>

```
card_num = card.cardnumber()
```



## Class Cardpack

카드 팩 만들기
<br>

```
cardpack = Cardpack(int : number_of_cardpack)
```
