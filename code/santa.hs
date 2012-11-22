import Data.List (tails, isPrefixOf, permutations)

type Pair = (Person, Person)
type Combination = [Pair]
data Person = Person { first:: String, lastn:: String } deriving (Show, Eq)

input = ["Luke Skywalker",
	"Leia Skywalker",
        "Toula Portokalos",
        "Gus Portokalos",
        "Bruce Wayne",
        "Virgil Brigman",
        "Lindsey Brigman"]

is_valid:: Pair -> Bool
is_valid (a, b) = (a /= b) && (lastn a /= lastn b)

valid_comb:: Combination -> Bool
valid_comb comb = all is_valid comb

combinations:: [Person] -> [Combination]
combinations pers =
    map (\x -> zip x pers) $ permutations pers

make_person:: String -> Person
make_person person =
    let [first, last] = splitByDelimiter ' ' person
    in Person first last


splitByDelimiter :: Char -> String -> [String]
splitByDelimiter _ "" = []
splitByDelimiter delimiter list =
  map (takeWhile (/= delimiter) . tail)
    (filter (isPrefixOf [delimiter])
       (tails
           (delimiter : list)))


people:: [Person]
people = map make_person input

all_combs:: [Combination]
all_combs = combinations people
valid_combs = filter valid_comb all_combs

main = do
    print $ length all_combs
    print $ length valid_combs
    mapM_ print (take 10 $ filter valid_comb all_combs)