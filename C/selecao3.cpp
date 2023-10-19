#include <map>

template<typename K, typename V>
class interval_map {
	friend void IntervalMapTest();
	V m_valBegin;
	std::map<K,V> m_map;
public:
	// constructor associates whole range of K with val
	interval_map(V const& val)
	: m_valBegin(val)
	{}

	// Assign value val to interval [keyBegin, keyEnd).
	// Overwrite previous values in this interval.
	// Conforming to the C++ Standard Library conventions, the interval
	// includes keyBegin, but excludes keyEnd.
	// If !( keyBegin < keyEnd ), this designates an empty interval,
	// and assign must do nothing.
	void assign( K const& keyBegin, K const& keyEnd, V const& val ) {
		if (!(keyBegin < keyEnd)) {
			return;
		}

		// Find the first element in m_map with a key greater than or equal to keyBegin
		auto itBegin = m_map.lower_bound(keyBegin);

		// Check if itBegin points to the beginning of the map or if the previous element has a different value
		bool insertBegin = (itBegin == m_map.begin() || (--itBegin)->second != val);

		// If insertBegin is true, we need to check if itBegin's key is greater than keyBegin
		// and if it is, we should create a new entry in m_map with the keyBegin and val.
		if (insertBegin && itBegin->first != keyBegin) {
			m_map[keyBegin] = val;
		}

		// Find the first element in m_map with a key greater than or equal to keyEnd
		auto itEnd = m_map.lower_bound(keyEnd);

		// Check if itEnd points to the end of the map or if the previous element has a different value
		bool insertEnd = (itEnd == m_map.end() || itEnd->second != val);

		// Erase elements between itBegin and itEnd
		m_map.erase(++itBegin, itEnd);

		// If insertEnd is true, we need to check if itEnd's key is greater than keyEnd
		// and if it is, we should create a new entry in m_map with the keyEnd and the previous value.
		if (insertEnd && itEnd->first != keyEnd) {
			m_map[keyEnd] = itEnd->second;
		}
	}

	// look-up of the value associated with key
	V const& operator[]( K const& key ) const {
		auto it = m_map.upper_bound(key);
		if (it == m_map.begin()) {
			return m_valBegin;
		} else {
			return (--it)->second;
		}
	}
};

// Função de teste externa
void IntervalMapTest() {
	// Teste 1: Criar um interval_map com um valor inicial
	interval_map<int, char> M('A');

	// Deve produzir a seguinte representação:
	// -∞ -> 'A'
	// Teste 2: Atribuir um intervalo [1, 4) com 'B'
	M.assign(1, 4, 'B');

	// Deve produzir a seguinte representação:
	// -∞ -> 'A'
	// 1 -> 'B'
	// 4 -> 'A'

	// Teste 3: Atribuir um intervalo [2, 6) com 'C'
	M.assign(2, 6, 'C');

	// Deve produzir a seguinte representação:
	// -∞ -> 'A'
	// 1 -> 'B'
	// 2 -> 'C'
	// 6 -> 'A'

	// Teste 4: Atribuir um intervalo [3, 5) com 'D'
	M.assign(3, 5, 'D');

	// Deve produzir a seguinte representação:
	// -∞ -> 'A'
	// 1 -> 'B'
	// 2 -> 'C'
	// 3 -> 'D'
	// 5 -> 'C'
	// 6 -> 'A'

	// Teste 5: Atribuir um intervalo [0, 7) com 'E'
	M.assign(0, 7, 'E');

	// Deve produzir a seguinte representação:
	// -∞ -> 'E'
	// 7 -> 'A'

	// Teste 6: Atribuir um intervalo [7, 10) com 'F'
	M.assign(7, 10, 'F');

	// Deve produzir a seguinte representação:
	// -∞ -> 'E'
	// 7 -> 'F'
	// 10 -> 'A'
}

int main() {
	IntervalMapTest();
	return 0;
}
