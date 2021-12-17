doubleMe x = x + x
doubleUs x y = x*2 + y*2
doubleThem x y z = doubleUs x y + doubleMe z
doubleSmallNumber x = if x > 100 then x else x*2
doubleBigNumber x = if x < 100 
                then x 
                else x*2
doubleSmallNumber' x = (if x > 100 then x else x*2) + 1
conanO'Brien = "It's a-me, Conan O'Brien!"
glueUs x y = x ++ y
glueMeTo x y = x:y