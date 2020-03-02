rm *.hi *.o
rm WhileParser
ghc -main-is WhileParser -o WhileParser WhileParser.hs
