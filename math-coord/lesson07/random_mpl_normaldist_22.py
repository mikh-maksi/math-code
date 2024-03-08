import statistics as st
sat = st.NormalDist(1060, 195)
print(sat)

print(sat.cdf(1200 + 0.5))
print(sat.pdf(1001))

print(sat.samples(10))