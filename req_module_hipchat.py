#!/usr/bin/env python


def request(self, method, url, **kwargs):
    if self.dump_reqs:
        print >> sys.stderr, "REQUEST", method, url
    while True:
        try:
            if self.rl_remaining <= 0:
                # We're out of requests, chill
                self._rl_sleep(self.rl_reset)
            resp = super(_requests, self).request(method, url, **kwargs)
        except HttpTooManyRequests as e:
            self.rl_remaining = int(e.response.headers['x-ratelimit-remaining'])
            if not self.rl_remaining:
                self.rl_reset = float(e.response.headers['x-ratelimit-reset'])
                continue  # Try the request again
            else:
                raise
        else:
            self.rl_remaining = int(resp.headers['x-ratelimit-remaining'])
            self.rl_reset = float(resp.headers['x-ratelimit-reset'])
            return resp
