# Hoofdstuk 1: Java
## Collections

### List<E>

- Een List is een geordende collectie van elementen, die duplicaten kan bevatten. Elk element heeft een index, en je kunt toegang krijgen tot elementen via hun positie in de lijst.
- Dit zijn de verschillende soorten lijsten:
  - **ArrayList<E>**
	 - Een dynamische array die groeit naarmate er elementen worden toegevoegd. Voordeel is snelle willekeurige toegang.
  - **LinkedList<E>**
	 - Gebaseerd op een dubbel-gekoppelde lijst, waardoor het sneller is voor het invoegen/verwijderen van elementen, maar langzamer voor willekeurige toegang.
- Belangrijkste methodes:
  - **add(E element)**:
	 - Voeg een element toe aan het einde van de lijst.
  - **get(int index)**:
	 - Haal het element op een bepaalde index op.
  - **remove(int index)**:
	 - Verwijder het element op een bepaalde index.
  - **size()**:
	 - Geeft het aantal elementen in de lijst terug.
  - **contains(Object o)**:
	 - Controleert of de lijst een bepaald element bevat.
  - **isEmpty()**:
	 - Controleert of de lijst leeg is.

### Set<E>

- Een Set is een collectie die geen duplicaten bevat. Een Set heeft geen volgorde voor de elementen, tenzij je een specifieke implementatie zoals TreeSet gebruikt.
- Dit zijn de verschillende soorten lijsten:
  - **HashSet<E>**:
	 - Gebaseerd op een hash-tabel, biedt snelle toegang tot elementen, maar zonder enige volgorde.
  - **LinkedHashSet<E>**:
	 - Zoals HashSet, maar behoudt de volgorde waarin elementen worden toegevoegd.
  - **TreeSet<E>**:
	 - Een Set die de elementen in gesorteerde volgorde opslaat (natuurlijke of op basis van een Comparator).
- Belangrijkste methoden:
  - **add(E element)**:
	 - Voeg een element toe aan de set (voegt alleen toe als het element nog niet bestaat).
  - **remove(Object o)**:
	 - Verwijder een element uit de set.
  - **contains(Object o)**:
	 - Controleer of een element aanwezig is in de set.
  - **size()**:
	 - Geeft het aantal elementen in de set terug.
  - **isEmpty()**:
	 - Controleert of de set leeg is.

### Queue<E>

- Een Queue is een collectie die elementen op een bepaalde volgorde opslaat, meestal volgens het "First-In-First-Out" (FIFO)-principe. Sommige implementaties ondersteunen andere volgordes zoals prioriteitsvolgorde.
- Belangrijkste methoden:
  - **offer(E element)**:
	 - Voeg een element toe aan de queue.
  - **poll()**:
	 - Haal en verwijder het element aan de voorkant van de queue (of retourneer null als de queue leeg is).
  - **peek()**:
	 - Haal op, maar verwijder het element aan de voorkant van de queue (of retourneer null als de queue leeg is).
  - **isEmpty()**:
	 - Controleer of de queue leeg is.
  - **size()**:
	 - Geeft het aantal elementen in de queue terug.

### Deque<E> (Double-Ended Queue)

- Een Deque is een uitbreiding van Queue waarbij je elementen aan beide zijden (begin en eind) kunt toevoegen en verwijderen. Dit biedt meer flexibiliteit dan een gewone Queue.
- Dit zijn de verschillende soorten lijsten:
  - **ArrayDeque<E>**:
	 - Een zeer efficiënte implementatie van een Deque zonder capaciteitslimiet
- Dit zijn de belangrijkste methoden:
  - **addFirst(E element)**:
	 - Voeg een element toe aan het begin van de deque.
  - **addLast(E element)**:
	 - Voeg een element toe aan het einde van de deque.
  - **removeFirst()**:
	 - Verwijder het eerste element.
  - **removeLast()**:
	 - Verwijder het laatste element.
  - **getFirst()**:
	 - Haal het eerste element zonder te verwijderen.
  - **getLast()**:
	 - Haal het laatste element zonder te verwijderen.

### Stack<E>

- Een Stack is een LIFO (Last-In-First-Out) collectie. Je voegt elementen toe en haalt ze af van de bovenkant van de stack.
- Dit zijn de verschillende soorten lijsten:
  - **push(E element)**:
	 - Voeg een element toe aan de bovenkant van de stack.
  - **pop()**:
	 - Verwijder en retourneer het bovenste element van de stack.
  - **peek()**:
	 - Bekijk het bovenste element zonder het te verwijderen.
  - **isEmpty()**:
	 - Controleer of de stack leeg is.
  - **size()**:
	 - Geeft het aantal elementen in de stack terug.

### Map<E>

- Een Map slaat paren van sleutels en waarden op. Elke sleutel is uniek, en je kunt de waarde ophalen via de sleutel.
- Dit zijn de verschillende soorten lijsten:
  - **HashMap<K, V>**:
	 - De meest gebruikte implementatie, gebaseerd op hashing, biedt snelle toegang tot elementen.
  - **LinkedHashMap<K, V>**:
	 - Zoals HashMap, maar behoudt de volgorde waarin de elementen zijn toegevoegd.
  - **TreeMap<K, V>**:
	 - Slaat de sleutel-waardeparen in gesorteerde volgorde op, gebaseerd op de natuurlijke volgorde van de sleutels of een Comparator.
- Dit zijn de belangrijkste methoden:
  - **put(K key, V value)**:
	 - Voeg een sleutel-waarde paar toe.
  - **get(Object key)**:
	 - Haal de waarde op bij de opgegeven sleutel.
  - **remove(Object key)**:
	 - Verwijder het paar met de opgegeven sleutel.
  - **containsKey(Object key)**:
	 - Controleer of de map een bepaalde sleutel bevat.
  - **size()**:
	 - Geeft het aantal sleutel-waardeparen in de map terug.
- Overlopen van een map:
```java
String result = map.entrySet()
                .stream()
                .map(entry -> "Key: " + entry.getKey() + ", Value: " + entry.getValue())
					 //.map(entry -> "key: %s, value: %s".formatted(entry.getKey(), entry.getValue()))
                .collect(Collectors.joining("\n"))
```

### Verschil met Iterator en ListIterator

- Iterator is enkel om enkel te overlopen/verwijderen
- ListIterator kan je de lijst aanpassen via bv. `set()`

### Mogelijke examenvraag: wanneer gebruik je een linkedlist en wanneer een arraylist

- LinkedList: Handig als je moet inserten en deleten
- ArrayList: Handig als je moet opvragen

### Samenvatting Collections Framework

![alt text](../Advanced_Software_Development_1/)

## Streams

### Immutibla vs mutable

- Een immutable collectie kan niet worden aangepast nadat deze is gemaakt. Dit betekent dat je geen elementen kunt toevoegen, verwijderen of wijzigen in de lijst.

  - Je bereikt dit door aan het einde van je stream het volgende toe te voegen:
  ```java
    lijst.stream().collect(Collectors.toList());
    ```
  - er zijn ook andere mogelijk, zoals `toSet()`

- Mutable: Een mutable lijst kan na het maken nog worden aangepast. Je kunt elementen toevoegen, verwijderen of wijzigen.
  - Je bereikt dit door aan het einde van je stream het volgende toe te voegen:
  ```java
    lijst.stream().toList()
    ```

### Oplossen van een encapsulatielek / zorgen dat een lijst onveranderbaar is

```java
return Collections.unmodifiableCollection(sportersLijst);
```

### DOA (Data Access Object)

- DAO is een ontwerppatroon dat wordt gebruikt om toegang te krijgen tot gegevens vanuit een database of een andere opslagbron. Het idee is om de toegang tot de gegevensbron te scheiden van de business logica. Een DAO is verantwoordelijk voor het uitvoeren van CRUD-operaties (Create, Read, Update, Delete) op de database.

### JPA (Java Persistence API)

- JPA is een specificatie binnen de Java EE/ Jakarta EE-omgeving die helpt bij het mappen van Java-objecten op relationele databases. Het is geen bibliotheek of framework op zich, maar een reeks richtlijnen die worden geïmplementeerd door frameworks zoals Hibernate, EclipseLink of OpenJPA.

## Generics

**Wat zijn generieke methoden**
* Dit zijn methoden waarbij meerdere datatypes mogelijk zijn
* Het maakt dus niet uit welke types hier worden ingestoken

### Generieke methodes
**Voorbeeld**
* Je hebt 3 arrays die maar allemaal met een verschillend en je wil die afprinten
* Het probleem is dat je drie verschillende methoden moet schrijven waarbij enkel het type van de parameter verschillend is:
```java
public static void printArray(Character[] /* Integer, String */ inputArray ){
	Stream.of(inputArray).forEach(element -> System.out.printf("%s ", element));
}
```

* Dit is op te lossen met een generieke methode waardoor meerdere datatypes in deze lijst kunnen zijn
```java
public static <E> void printArray(E[] /* Integer, String */ inputArray ){
	Stream.of(inputArray).forEach(element -> System.out.printf("%s ", element));
}
```
**Belangrijk**
* Meerdere parameters kunnen hier hetzelfde generieke type (E) krijgen
* Om bv. een generieke maximumMethode te implementeren kunnen we gebruik maken van `Comparable`:
```java
public static < T extends Comparable< T > > T maximum( T x, T y, T z ){
	T max = x; 
	if ( y.compareTo( max ) > 0 )
		max = y; 
	if ( z.compareTo( max ) > 0 )
		max = z; 

	// via streams
	// T max = Arrays.asList(x,y,z).stream().max(T::compareTo).get();
	return max;
}
```

### Generieke klassen
Hier is een voorbeeld van een generieke klasse door een eigen `Stack`-implementatie te bouwen:

```java
public class Stack<E>{
	private final int SIZE; 
	private int top; 
	private E[] elements; 

	public Stack(){
		this( 10 );
	}

	public Stack( int s ){
		SIZE = s > 0 ? s : 10; 
		top = -1; 
		elements = (E[]) new Object[SIZE]; // creatie van de array
	}

	public void push(E pushValue) {
		if ( top == SIZE - 1 ) 
			throw new FullStackException( String.format("Stack is full, cannot push %s ", pushValue ));
		elements[ ++top ] = pushValue; // plaats op de stack
	} 

	public E pop() {
		if ( top == -1 ) 
			throw new EmptyStackException( "Stack is empty, cannot pop" );
		return elements[ top-- ]; // verwijder en geef het top element terug
	}
}
```

### Wildcards
Wildcards worden gebruikt om flexibiliteit te introduceren bij het werken met generics in methodes of klassen.


* **Upperbound wildcard**
	* Een **upperbound** wildcard wordt gebruikt als je wilt beperken dat een type maximaal een bepaald supertype mag zijn:
```java
public static double sum(Collection<? extends Number> list) {
    return list.stream().mapToDouble(Number::doubleValue).sum();
}
```
**Uitleg**
* `<? extends Number>` betekent dat list elk type kan bevatten dat Number is of een subtype daarvan (bijvoorbeeld `Integer, Double`, enz.).
* Hierdoor kun je een lijst van verschillende `Number`-subtypes doorgeven en veilig werken met hun methodes. 

* **LowerBound wildcard**
Een lowerbound wildcard wordt gebruikt als je wilt beperken dat een type minimaal een bepaald subtype mag zijn:
```java
public static void addIntegers(List<? super Integer> list) {
    list.add(10);
    list.add(20);
}
```

**Uitleg**
* `<? super Integer>` betekent dat `list` elk type kan bevatten dat `Integer` is of een supertype daarvan (bijvoorbeeld `Number, Object`).
* Dit is nuttig als je elementen wilt toevoegen, omdat Java anders niet weet welk type hij moet accepteren.

### Belangrijke termen bij wildcards
* `?` **(unbounded wildcard)**:
	* Staat voor "ik weet niet wat het type is".
	* Wordt gebruikt als je een generieke methode flexibel wilt maken, zonder restricties:
```java
public static void printList(List<?> list) {
    for (Object elem : list) {
        System.out.println(elem);
    }
}
```
* **Upperbound wildcard (`extends`):**
	* Gebruik `? extends T` als je gegevens **alleen wilt lezen** en **niet wilt schrijven**.
	* Dit zorgt ervoor dat je veilig toegang hebt tot de methodes van T.

* **Lowerbound wildcard (`super`)**:
	* Gebruik `? super T` als je gegevens **alleen wilt schrijven** en **niet wilt lezen**.
	* Dit zorgt ervoor dat je veilig elementen kunt toevoegen aan een collectie.

### Andere belangrijke punten over generics
1. **Type-erasure**:	
	* Tijdens compilatie vervangt Java alle generieke types door hun "raw type" (zoals `Object`), en voegt indien nodig casts toe.
	* Dit betekent dat generics puur syntactische controle tijdens compileertijd bieden.

2. **Generics en primitive types:**
	* Generics werken niet met primitive types zoals int of double. Gebruik in plaats daarvan hun wrapper-klassen (Integer, Double, enz.).

3. **Generics in method chaining:**
	* Generics maken method chaining mogelijk, zoals in builder-patronen, door hetzelfde generieke type terug te geven:
```java
public class Builder<T> {
    private T value;

    public Builder<T> setValue(T value) {
        this.value = value;
        return this;
    }

    public T build() {
        return value;
    }
}
```
4. **Niet-generieke klassen kunnen erven van generieke klassen:**

Een niet-generieke klasse kan erven van een generieke klasse door een type vast te zetten:
```java
public class StringStack extends Stack<String> { }
```

## Observer Pattern

## Netwerken

### Inleiding
* Netwerkprogrammeren draait om communicatie tussen computers **via het internet of een lokaal netwerk**.
* Twee **communicatieprincipes**:
	* **Stream-based** communicatie (bijvoorbeeld TCP): Gegevens worden continu als een stroom verzonden.
	* **Packet-based** communicatie (bijvoorbeeld UDP): Gegevens worden in afzonderlijke pakketten verzonden.
* **Client/Server-model**:
	* **Client**: Stelt een verzoek in via een netwerk.
	* **Server**: Behandelt het verzoek en stuurt een antwoord terug.
	* Dit model volgt het **request-response-principe** (zoals webbrowsers en webservers).

### Sockets
* **Sockets** zijn softwareobjecten die eindpunten van een netwerkverbinding vertegenwoordigen.
* **Stream Sockets** gebruiken TCP voor een **verbinding-georiënteerde service**.
* Sockets lijken op file I/O: een server of client opent een connectie, stuurt/ontvangt gegevens, en sluit de connectie.

### Een server in 5 stappen:

Maken van een **ServerSocket**:
```java
ServerSocket server = new ServerSocket(portNumber, queueLength);
```

* De server bindt zich aan een poort waarop hij luistert naar inkomende connecties.
* Geldige poortnummers: 1024 - 65535 (poorten < 1024 zijn gereserveerd voor systeemservices).
* **Luister naar connecties:**
```java
Socket connection = server.accept();
```
* Deze methode blokkeert totdat een client verbinding maakt.

* **Verkrijg I/O streams:**
* Voor communicatie met de client:
```java
OutputStream output = connection.getOutputStream();
InputStream input = connection.getInputStream();
```
* Gegevens worden via de **streams verzonden en ontvangen**.
* **Sluit de connectie:**
Sluit de socket en de streams met de methode close.
```java
socket.close();
```

### Bouwen van een client
* **Creëer een Socket:**
```java
Socket connection = new Socket(serverAddress, portNumber);
```
* Maakt verbinding met de server op het opgegeven adres en poort.

* **Verkrijg I/O streams:**
* Gebruik `getInputStream() en getOutputStream()` om referenties naar de streams te krijgen.

* **Communiceer met de server:**
Wissel gegevens uit via de streams.

* **Sluit de connectie:**
Sluit de socket en streams met de methode close.

# Hoofdstuk 2: Test Driven Development
## JUnit
**Test Triven Development**
* Je schrijft testcode nog voor je de echte code gaat schrijven
* Maar om rode lijntjes te vermijden is het de bedoeling dat je alsnog de **file aanmaakt** en **alle methoden** zonder uitwerking

### Een test maken die slaagt

- Je voert de functie uit als gewoon
- Via de `assertEquals` wordt er gekeken of de waarde geldig is

```java
public void Waterfles_vulDeFlesBij_deWaterFlesWordtGevuld(){
	int hoeveelheidBijTeVullen = 500;
	fles.vulBij(hoeveelheidBijTeVullen);
	Assertions.assertEquals(hoeveelheidBijTeVullen, fles.getHoeveelheid());
}
```

### Een test maken die hoort te falen

- Deze test bekijkt of de juiste exception wordt geworpen

```java
public void Waterfles_vulDeFlesBij_vultDeFlesMetEenNegatieveWaarde_WerptException(){
	int hoeveelheidBijTeVullen = -50;
	Assertions.assertThrows(IllegalArgumentException.class, () ->
			fles.vulBij(hoeveelheidBijTeVullen));
}
```

### @ParameterizedTest
* Om testen te vermijden met bijna exact dezelfde code gebruiken **ParameterizedTest** 
* Zo kunnen we verschillende waarden testen in dezelfde test zonder hem meerdere malen te testen
#### ValueSource

- Een valuesource zijn allemaal waarden die 1 zelfde test zullen doorgaan

```java
@ParameterizedTest
@ValueSource(ints = {1, 2, 3, 4, 5})
```

- ints kan ook de waarde hebben als:
  - ints: longs: doubles:shorts: bytes: chars: strings

#### @CsvSource

- Dit wordt gebruikt voor het leveren van meerdere invoerwaarden aan een parameterized test in CSV-formaat (Comma-Separated Values).

```java
@ParameterizedTest
    @CsvSource({
        "add, 1, 2, 3",
        "subtract, 5, 3, 2",
        "multiply, 2, 3, 6"
    })
    void testWithMultipleParams(String operation, int a, int b, int expectedResult) {
        int result = 0;
        switch (operation) {
            case "add": result = a + b; break;
            case "subtract": result = a - b; break;
            case "multiply": result = a * b; break;
        }
        assertEquals(expectedResult, result);  // Controleert of het resultaat correct is
    }
```

#### @EnumSource

- Wordt gebruikt om waarden van een enum door te geven aan een parameterized test.

```java
enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY
}

@ParameterizedTest
@EnumSource(Day.class)
```

#### @MethodSource

- Maakt het mogelijk om waarden dynamisch te genereren via een methode. De methode moet een Stream, Iterable, of array van waarden retourneren.

```java
static Stream<String> stringProvider() {
        return Stream.of("JUnit", "MethodSource", "Parameterized");
}

@ParameterizedTest
@MethodSource("stringProvider")
```

#### @NullAndEmptySource

- Combineert de functionaliteit van @NullSource en @EmptySource. Dit betekent dat je een test kunt uitvoeren met zowel null als een lege string (of lege collecties).

```java
@ParameterizedTest
@NullAndEmptySource
void testWithNullAndEmptySource(String input) {
    assertTrue(input == null || input.isEmpty());
}
```

#### @NullSource

- Levert de waarde null aan een parameterized test. Dit is handig om te testen hoe methoden reageren op null input.

```java
@ParameterizedTest
@NullSource
void testWithNullSource(String input) {
    assertNull(input);  // De input moet null zijn
}
```

#### @EmptySource

- levert een lege waarde aan de test, zoals een lege string "", een lege collectie, of een lege array.

```java
@ParameterizedTest
@EmptySource
void testWithEmptySource(String input) {
    assertTrue(input.isEmpty());  // Controleert of de invoer leeg is
}
```

## Mockito Framework
**Integreren van Mocktio**
```java
@ExtendWith(MockitoExtension.class)
```

**Mock-object maken en object waarop we gaan testen**
* InjectsMock dient om de klasse te mocken dat een associatie heeft met FactuurMap
```java
	@Mock
	private FactuurMap factuurMap;	
	
	@InjectsMock
	private Boekhouding b;
``` 

**Met deze objecten kunnen we dan de test uitvoeren**
* Als het de bedoeling is dat een methode 0 keer wordt uitgetest kunnen we gebruik maken van `Mockito.lenient().when(...)`
* Mock trainen zonder lenient: we krijgen een extra controle: de methode van de mock moet minstens één keer opgeroepen worden. 
* Mock trainen met lenient: de extra controle ongedaan maken

```java
private Stream<Arguments> juisteAangiftes(){
		Stream.of(Arguments.of(Boekhouding.BELASTINGSCHAAL_1), new double[] {100.00, 200.25});
		Stream.of(Arguments.of(Boekhouding.BELASTINGSCHAAL_0), new double[] {100.00, 50.25});
		Stream.of(Arguments.of(Boekhouding.BELASTINGSCHAAL_0), new double[] {0.0, 0.0});
		Stream.of(Arguments.of(Boekhouding.BELASTINGSCHAAL_0), new double[] {199.99, 0.0});
		Stream.of(Arguments.of(Boekhouding.BELASTINGSCHAAL_0), new double[] {100.00, 99.99});
		Stream.of(Arguments.of(Boekhouding.BELASTINGSCHAAL_1), new double[] {100.00, 100.00});
		Stream.of(Arguments.of(Boekhouding.BELASTINGSCHAAL_1), new double[] {0.0, 200.00});
		Stream.of(Arguments.of(Boekhouding.BELASTINGSCHAAL_1), new double[] {150.00, 200.25});
	}
	
	@Test
	@MethodSource("juisteAangiftes")
	void testGoedeGevallenMetJuisteAangifte(double schaal, double[] waardes) {
		Mockito.when(f.geefBedragen(CORRECT_ONDERNEMINGSNUMMER)).thenReturn(waardes);
		
		
		Aangifte expected = new Aangifte(schaal, waardes);
		Aangifte real = b.genereerAangifte(CORRECT_ONDERNEMINGSNUMMER);
		
		assertEquals(schaal, real.belastingSchaal());
		assertArrayEquals(waardes, real.bedragen());
		
		Mockito.verify(f, Mockito.times(1)).geefBedragen(CORRECT_ONDERNEMINGSNUMMER);
	}
```

# Hoofdstuk 3: Design Patterns   
## Strategy Pattern
**Wat is dit Design Pattern?**
* Wanneer objecten met overerving (Eend -> RubberenEend, HoutenEend ...) bepaalde eigenschappen hebben hoeft niet iedereen exact dezelfde waarden van die eigenschappen over te erven.
* Een normale eend kan bv. vliegen en kwaken terwijl een rubbereneend beide niet kan.
* Dit probleem kunnen we dus oplossen met het gebruik van interfaces.

**Ontwerpprincipes:**
* Bepaal de aspecten van je applicatie die variëren en scheid deze van de aspecten die hetzelfde blijven
* Programmeer naar een interface, niet naar een implementatie.
   * M.a.w. we gaan voor ieder gedrag een interface gebruiken, bv. FlyBehavior en QuackBehavior, en iedere implementatie van een gedrag implementeert één van deze interfaces.

**Implementatie**
* Hier hebben onze eenden twee over te erven attributen
   * Vlieg
   * Kwaak
* We maken dus twee interfaces voor deze attributen:
```java
public interface VliegGedrag {
	public String vlieg();
}
```
* Eenmaal de hoofdinterface is gemaakt, maken we nog een maken we nog normale klassen aan die de effectieve waarden zullen bevatten van de atrributen
* Voor VliegGedrag is dat dan:
   * VliegWel
   * VliegNiet
```java
public class VliegWel implements VliegGedrag{

	@Override
	public void vlieg() {
		Systen.out.print("Ik kan vliegen");
	}
}
```

* Eenmaal we al onze attribuutklassen hebben kunnen we de domeinklasse ervoor aanmaken:
```java
public abstract class Eend {
    private QuackGedrag kwaakGedrag;
    private VliegGedrag vliegGedrag;
    private SoortEend soortEend;

    public Eend(QuackGedrag kwaakGedrag, VliegGedrag vliegGedrag, SoortEend soortEend) {
        this.kwaakGedrag = kwaakGedrag;
        this.vliegGedrag = vliegGedrag;
        this.soortEend = soortEend;
    }

    public void kwaak() {
        kwaakGedrag.kwaak();
    }

    public void vlieg() {
        vliegGedrag.vlieg();
    }
}
```

* We kunnen de applicatie starten met volgende code:
```java
public void overloopEenden() {
	for (Eend eend : eenden) {
		eend.kwaak();
		System.out.println();
	   eend.vlieg();
		System.out.println();
		eend.getSoortEend();
		System.out.println();
	}
}
```

## Simple Factory
**Wat is dit Design Pattern?**
* In dit design pattern handelen we keuzes af
* Wanneer we bv. keuzemenuutjes moeten aanpassen is het de bedoeling dat we van dat menu een Factory-klasse maken
* In die factory is de default-keuze ook automatisch een klasse

**Implementatie**
* Stel we hebben een shop waar mensen moeten kiezen uit een menu en dit menu kan veranderen dan hebben we dit design pattern nodig
* We beginnen met het maken van onze pizza-object
```java
public abstract class Pizza {

	public void prepare() {
		System.out.println("Preparing " + getClass().getSimpleName());
	}
	
	public void deliver() {
		System.out.println("Your " + getClass().getSimpleName() + " is ready");
	}

}
```
* Waarbij we ook een paar soorten pizza's zullen aanmaken:
* Deze kan leeg zijn vanwege de manier hoe ik Pizza heb opgebouwd
```java
public class KaasPizza extends Pizza{

}
```

* Daarna implementeren we onze shop
```java
public class PizzaStore {
	private PizzaFactory factory = new PizzaFactory();
	
	public Pizza bestelPizza(String teBestellenPizza) {
		Pizza pizza;
		
		pizza = factory.orderPizza(teBestellenPizza);
		
        pizza.prepare();
        pizza.deliver();
        
        return pizza;
	}
}
```

* Het bestellen van de pizza (via dat menuutje) gebeurt dan via de PizzaFactory
```java
public class PizzaFactory {
    public Pizza orderPizza(String typePizza) {
        Pizza pizza = null;

        switch (typePizza) {
            case "barbeque":
                pizza = new BarbequePizza();
                break;
            case "kaas":
                pizza = new KaasPizza();
                break;
            case "margaritta":
                pizza = new Margaritta();
                break;
            default:
                pizza = new NonExistentPizza(typePizza);
        }
        
        return pizza; 
    }
}
```

* Het is ook de bedoeling dat als de opgegeven keuze (hier een pizza) niet bestaat dat we een object maken voor dit soort resultaten
```java
public class NonExistentPizza extends Pizza{
	private String opgegvenPizza;
	
	public NonExistentPizza(String opgegvenPizza) {
		this.opgegvenPizza = opgegvenPizza;
	}
	@Override
	public void prepare() {
		System.out.println(opgegvenPizza + " does not exist in our store");
	}
	
	@Override
	public void deliver() {
		System.out.println(opgegvenPizza + " this does not exist in our store");
	}
}
```

* Laten we wat pizza's bestellen!
```java
public class PizzaApplicatie {
	private PizzaStore pizzaStore;
	
	public PizzaApplicatie() {
		pizzaStore = new PizzaStore();
		this.initialiseerMethodes();
	}

	private void initialiseerMethodes() {
		this.bestelPizzas();
	}

	private void bestelPizzas() {
		// pizzaStore.bestelPizza("barbeque");
		pizzaStore.bestelPizza("kaas");
		pizzaStore.bestelPizza("nietBestaandePizza");

	}
}
```

## Observer Pattern
**Wat is dit Design Pattern?**
* Dit pattern streeft ernaar om eenvoudig en dynamisch tekst op schermen te laten verschijnen en ze te laten updaten zonder problemen
* Streef naar ontwerpen met een zwakke koppeling tussen de objecten die samenwerken..

**Implementatie**
* Maak twee interfaces:

* Subject
```java
public interface Subject {
	public void addObserver(Observer observer);
	public void removeObserver(Observer observer);
}
```

* Observer
```java
public interface Observer {
    /* variabelen die moeten geupdatetet worden  */
	public void update(double temperature, double luchtdruk);
}
```

* De klasse die hier **Subject** implementeert krijgt hier volgende attributen:
```java
	private Set<Observer> observers;
	
	public WeerStation(double temperature, double luchtdruk) {
		this.temperature = temperature;
		this.luchtdruk = luchtdruk;
		observers = new HashSet<>();
	}

    @Override
	public void addObserver(Observer observer) {
		observers.add(observer);
	}
	
	@Override
	public void removeObserver(Observer observer) {
		observers.remove(observer);
	}
	
	public void notifyObservers() {
		observers.forEach(observer -> observer.update(temperature, luchtdruk));
	}
```	

## Decorator Pattern
**Wat is dit Design Pattern?**
* Het doel is om klassen eenvoudig te kunnen uitbreieden om nieuw gedrag te incorporeren zonder de bestaande code te wijzigen
* Dit gaan we doen door allerlei booleans toe te voegen aan onze hoofdklasse waarvan iedereen gaat erven

**Implementatie**
* We beginnen met het maken van onze abstracte hoofdklasse
* We maken een beschrijving die we later nog gaan aanvullen met de echte waarde ervan en maken hier getters en setters voor
```java
public abstract class Drank {
    protected String description = "Unknown Beverage";

    public String getDescription() {
        return description;
    }
    
    public void setDescription(String description) {
    	this.description = description;
    }

    public abstract double cost();
}
```

* Dan beginnen we met de overerving en maken we drankjes aan voor onze koffieshop
```java
public class Espresso extends Drank {
    public Espresso() {
        setDescription("Espresso");
    }

    @Override
    public double cost() {
        return 1.99;
    }
}
```

* Daarna maken we een klasse dat hier de 'toppings' beheert, hier is dit dan onze Decorator
* Dit is een abstracte klasse dat een variabele bevat die we gaan 'decoreren'
```java
public abstract class DrankDecorator extends Drank {
    protected Drank drank; 

    public DrankDecorator(Drank drank) {
        this.drank = drank;
    }

    @Override
    public abstract String getDescription();
}
```

* Nu dit is gemaakt kunnen we een toppings/decorators maken
```java
public class Melk extends DrankDecorator{
	
	public Melk(Drank drank) {
		super(drank);
	}

	@Override
	public String getDescription() {
		return drank.getDescription() + " " + getClass().getSimpleName().toLowerCase();
	}

	@Override
	public double cost() {
		return drank.cost() + 0.10;
	}

}
```

* Voila onze decorator is klaar en nu kunnen we drankjes bestellen
```java
	private void bestelKoffies() {
		 drank = new Espresso();
		 System.out.println(drank.cost() + " -> " + drank.getDescription());
		 System.out.println();
		 
		 drank = new Melk(drank);
		 System.out.println(drank.cost() + " -> " + drank.getDescription());
		 System.out.println();
		 
		 drank2 = new Karamel(new Melk(drank2)) ;
		 System.out.println(drank2.cost() + " -> " + drank2.getDescription());
		 System.out.println();

	}
```

## State Pattern
**Wat is dit Design Pattern?**

**Implementatie**


## facade Pattern
**Wat is dit Design Pattern?**
* Dit werkt zoals de DomeinController dat we hebben gezien in jaar één
* We houden als onze klassen bij in één grote klasse
* Praat alleen met je directe vrienden. Hoe minder je weet hoe beter.

**Implementatie**
* We beginnen met ons object
```java
public class Game {
	private String naam;
	private double prijs;
	private int rating;
	
	public Game(String naam, double prijs, int rating) {
		setNaam(naam);
		setPrijs(prijs);
		setRating(rating);;
	}

	public String getNaam() {
		return naam;
	}

	private void setNaam(String naam) {
		this.naam = naam;
	}

	public double getPrijs() {
		return prijs;
	}

	private void setPrijs(double prijs) {
		this.prijs = prijs;
	}

	public int getRating() {
		return rating;
	}

	private void setRating(int rating) {
		this.rating = rating;
	}
	
	public double verhoogPrijs(double percentage) {
		return (this.prijs * (percentage * 100)) / 100;  
	}
	
}
```

* Gevolgt door onze facade
```java
public class GameFacade {
	private List<Game> games;

	public GameFacade() {
		this.games = new ArrayList<>();
		this.maakGames();
	}
	
	public void maakGames() {
		games.add(new Game("Elden Ring", 69.99, 4));
		games.add(new Game("Call of Duty Black Ops 6", 79.99, 4));
		games.add(new Game("Horizon Forbidden West", 59.99, 5));

	}
	
	public List<Game> geefGames(){
		return this.games;
	}
	
	public void verhoogPrijs(double percentage) {
		games.forEach(game -> game.verhoogPrijs(percentage));
	}
}
```

* Uiteindelijk kunnen we ze tonen in de applicatie
```java
public class GameApplicatie {

	private GameFacade gameFacade;
	
	public GameApplicatie(GameFacade gameFacade) {
		this.gameFacade = gameFacade;
		this.toonGamesInclusiefInflatie();
	}
	
	public void geefAlleGames() {
		for (Game game : gameFacade.geefGames()) {
			System.out.printf("Naam: %s - Prijs: %.2f - Rating - %d%n", game.getNaam(), game.getPrijs(), game.getRating());
		}
	}
	
	public void toonGamesInclusiefInflatie() {
		this.geefAlleGames();
		gameFacade.verhoogPrijs(10.00);
		System.out.println();
		this.geefAlleGames();
		
	}
}	
```

## MVC (Geen Design Pattern maar zit alsnog in dit hoofdstuk)
**Wat is dit Design Pattern?**

**Implementatie**
