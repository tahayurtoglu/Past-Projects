text = "X-DSPAM-Confidence:    0.8475"
f_t  = text.find(":")
desi_part = text[f_t+1:]
s_d_p = desi_part.strip()
print(float(s_d_p))
