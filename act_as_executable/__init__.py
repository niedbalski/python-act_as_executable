#!/usr/bin/env python

__author__ = 'Jorge Niedbalski R. <jnr@pyrosome.org>'

from string import Template
import envoy

def act_as_executable(command):

    DEFAULT_TIMEOUT = 10

    def wrapper(callback):
        def to_dict_filter(value):
            if not isinstance(value, dict):
                value = { 'response' : value }
            return value

        def apply_filters(cls, filters, response):
            ( cmd, status, output ) = response
            attr = '%s_filter' % (callback.__name__)
            if hasattr(cls, attr):
                output = getattr(cls, attr)(output)
            return to_dict_filter(output)

        def build_cmd(cmd, *args, **kwargs):
            if len(args) > 0:
                for idx, arg in enumerate(args):
                    kwargs.update({'args_%d' % idx: arg})
            return Template(cmd).safe_substitute(kwargs)

        def run(command, timeout=DEFAULT_TIMEOUT):
            def _r(cmd, timeout):
                r = envoy.run(cmd, timeout=timeout)
                return ( r.command, r.status_code, r.std_out)
            return _r(command, timeout)

        def wrapped_f(self, *args, **kwargs):
            response = apply_filters(
                self, callback, run(build_cmd(command, *args, **kwargs)))
            return callback(self, args, **response)

        return wrapped_f

    return wrapper

