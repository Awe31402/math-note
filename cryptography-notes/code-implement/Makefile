CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O2 -Iinclude

SRCDIR = src
INCDIR = include
BIN = crypto_demo

SRCS = $(SRCDIR)/main.cpp \
       $(SRCDIR)/DES.cpp \
       $(SRCDIR)/AES.cpp \
       $(SRCDIR)/GF256.cpp \
       $(SRCDIR)/BlockCipher.cpp \
       $(SRCDIR)/BigInt.cpp \
       $(SRCDIR)/RSA.cpp \
       $(SRCDIR)/RSADemo.cpp

OBJS = $(SRCS:.cpp=.o)

all: $(BIN)

$(BIN): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $^

$(SRCDIR)/%.o: $(SRCDIR)/%.cpp $(wildcard $(INCDIR)/*.hpp)
	$(CXX) $(CXXFLAGS) -c $< -o $@

test: $(BIN)
	./$(BIN)

trace: $(BIN)
	./$(BIN) --trace

clean:
	rm -f $(OBJS) $(BIN) /tmp/test_* /tmp/check_* /tmp/debug_*

.PHONY: all test trace clean
