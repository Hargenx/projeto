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
		// Check if the interval is empty (keyBegin >= keyEnd)
		if (!(keyBegin < keyEnd)) {
			return;
		}

		// Find the first element in m_map with a key greater than or equal to keyBegin
		auto itBegin = m_map.lower_bound(keyBegin);

		// Find the first element in m_map with a key greater than or equal to keyEnd
		auto itEnd = m_map.lower_bound(keyEnd);

		// Check if itBegin points to the beginning of the map or if the previous element has a different value
		bool insertBegin = (itBegin == m_map.begin() || (--itBegin)->second != val);

		// Check if itEnd points to the end of the map or if the previous element has a different value
		bool insertEnd = (itEnd == m_map.end() || itEnd->second != val);

		// Erase elements between itBegin and itEnd
		m_map.erase(itBegin, itEnd);

		// Insert the new interval if necessary
		if (insertBegin) {
			m_map[keyBegin] = val;
		}
		if (insertEnd) {
			m_map[keyEnd] = itEnd->second;
		}
	}
};
