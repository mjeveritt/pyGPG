#!/usr/bin/python
# -*- coding: utf-8 -*-
#################################################################################
# pyGPG LEGEND
#################################################################################
# File:       legend.py
#
#             LEGEND data for interpreting the results
#             of gpg operation status messages
#
# Copyright:
#             (c) 2012 Brian Dolbec
#             Distributed under the terms of the GNU General Public License v2
#
# Author(s):
#             Brian Dolbec <dolsen@gentoo.org>
#
'''Holds pyGPG's gpg status output legend.'''


from collections import namedtuple


# make this global, so is easy to change, and calculates only once
IDENTIFIER = '[GNUPG:] '
ID_LEN = len(IDENTIFIER)

class NEWSIG(namedtuple('NEWSIG', '')):
    msg = "Issued right before a signature verification starts."
    __slots__ = ()

class GOODSIG(namedtuple('GOODSIG', ['long_keyid', 'username'])):
    msg = "The signature with the keyid is good."
    __slots__ = ()

class EXPSIG(namedtuple('EXPSIG', ['long_keyid', 'username'])):
    msg = "The signature with the keyid is good, but the signature is expired."
    __slots__ = ()

class EXPKEYSIG(namedtuple('EXPKEYSIG', ['long_keyid', 'username'])):
    msg = "The signature with the keyid is good, but the signature was made by an expired key."
    __slots__ = ()

class REVKEYSIG(namedtuple('REVKEYSIG', ['long_keyid', 'username'])):
    msg = "The signature with the keyid is good, but the signature was made by a revoked key."
    __slots__ = ()

class BADSIG(namedtuple('BADSIG', ['long_keyid', 'username'])):
    msg = "The signature with the keyid has not been verified okay."
    __slots__ = ()

class ERRSIG(namedtuple('ERRSIG', ['long_keyid', 'pubkey_algo', 'hash_algo'
            'sig_class', 'timestamp', 'rc'])):
    msg = "It was not possible to check the signature."
    __slots__ = ()

class VALIDSIG(namedtuple('VALIDSIG', ['fingerprint', 'sig_creation_date', 'sig_timestamp',
            'expire_timestamp',  'sig_version', 'reserved', 'pubkey_algo',
            'hash_algo', 'sig_class','primary_key_fpr'])):
    msg = "The signature with the keyid is good."
    __slots__ = ()

class SIG_ID(namedtuple('SIG_ID', ['radix64_string', 'sig_creation_date', 'sig_timestamp'])):
    msg = "This is emitted only for signatures of class 0 or 1 which have been verified okay."
    __slots__ = ()

class ENC_TO(namedtuple('ENC_TO', ['long_keyid', 'keytype', 'keylength'])):
    msg = "The message is encrypted to this LONG_KEYID."
    __slots__ = ()

class NODATA(namedtuple('NODATA', 'what')):
    msg = \
"""No data has been found. Codes for what are:
    1 - No armored data.
    2 - Expected a packet but did not found one.
    3 - Invalid packet found, this may indicate a non OpenPGP
            message.
    4 - signature expected but not found
You may see more than one of these status lines."""
    __slots__ = ()

class UNEXPECTED(namedtuple('UNEXPECTED', 'what')):
    msg = "Unexpected data has been encountered, 0 - not further specified"
    __slots__ = ()

class TRUST_UNDEFINED(namedtuple('TRUST_UNDEFINED', 'error_token')):
    msg = ""
    __slots__ = ()

class TRUST_NEVER(namedtuple('TRUST_NEVER', 'error_token')):
    msg = "For good signatures, this indicates the validity of the key used to create the signature."
    __slots__ = ()

class TRUST_MARGINAL(namedtuple('TRUST_MARGINAL', 'validation_model')):
    msg = "For good signatures, this indicates the validity of the key used to create the signature."
    __slots__ = ()

class TRUST_FULLY(namedtuple( 'TRUST_FULLY', 'validation_model')):
    msg = "For good signatures, this indicates the validity of the key used to create the signature."
    __slots__ = ()

class TRUST_ULTIMATE(namedtuple('TRUST_ULTIMATE', 'validation_model')):
    msg = "For good signatures, this indicates the validity of the key used to create the signature."
    __slots__ = ()

class PKA_TRUST_GOOD(namedtuple('PKA_TRUST_GOOD', 'mailbox')):
    msg = "A status code emitted in addition to a TRUST_* status."
    __slots__ = ()

class PKA_TRUST_BAD(namedtuple('PKA_TRUST_BAD', 'mailbox')):
    msg = "A status code emitted in addition to a TRUST_* status."
    __slots__ = ()

class SIGEXPIRED(namedtuple('SIGEXPIRED', '')):
    msg = "This is deprecated in favor of KEYEXPIRED."
    __slots__ = ()

class KEYEXPIRED(namedtuple('KEYEXPIRED', 'expire_timestamp')):
    msg = "The key has expired.  expire_timestamp is the expiration time in seconds since Epoch."
    __slots__ = ()

class KEYREVOKED(namedtuple('KEYREVOKED', '')):
    msg = "The used key has been revoked by its owner."
    __slots__ = ()

class BADARMOR(namedtuple('BADARMOR', '')):
    msg = "The ASCII armor is corrupted."
    __slots__ = ()

class RSA_OR_IDEA(namedtuple('RSA_OR_IDEA', '')):
    msg = "The IDEA algorithms has been used in the data."
    __slots__ = ()

class SHM_INFO(namedtuple('SHM_INFO', '')):
    msg = ""
    __slots__ = ()

class SHM_GET(namedtuple('SHM_GET', '')):
    msg = ""
    __slots__ = ()

class SHM_GET_BOOL(namedtuple('SHM_GET_BOOL', '')):
    msg = ""
    __slots__ = ()

class SHM_GET_HIDDEN(namedtuple('SHM_GET_HIDDEN', '')):
    msg = ""
    __slots__ = ()

class GET_BOOL(namedtuple('GET_BOOL', '')):
    msg = ""
    __slots__ = ()

class GET_LINE(namedtuple('GET_LINE', '')):
    msg = ""
    __slots__ = ()

class GET_HIDDEN(namedtuple('GET_HIDDEN', '')):
    msg = ""
    __slots__ = ()

class GOT_IT(namedtuple('GOT_IT', '')):
    msg = ""
    __slots__ = ()

class NEED_PASSPHRASE(namedtuple('NEED_PASSPHRASE', ['long_main_keyid',
                                'long_keyid', 'keytype', 'keylength'])):
    msg = "Issued whenever a passphrase is needed."
    __slots__ = ()

class NEED_PASSPHRASE_SYM(namedtuple('NEED_PASSPHRASE_SYM', ['cipher_algo', 's2k_mode', 's2k_hash'])):
    msg = "Issued whenever a passphrase for symmetric encryption is needed."
    __slots__ = ()

class NEED_PASSPHRASE_PIN(namedtuple('NEED_PASSPHRASE_PIN', ['card_type', 'chvno', 'serialno'])):
    msg = "Issued whenever a PIN is requested to unlock a card."
    __slots__ = ()

class MISSING_PASSPHRASE(namedtuple('MISSING_PASSPHRASE', '')):
    msg = "No passphrase was supplied."
    __slots__ = ()

class BAD_PASSPHRASE(namedtuple('BAD_PASSPHRASE', 'long_keyid')):
    msg = "The supplied passphrase was wrong or not given."
    __slots__ = ()

class GOOD_PASSPHRASE(namedtuple('GOOD_PASSPHRASE', '')):
    msg = "The supplied passphrase was good and the secret key material is therefore usable."
    __slots__ = ()

class DECRYPTION_FAILED(namedtuple('DECRYPTION_FAILED', '')):
    msg = "The symmetric decryption failed - one reason could be a wrong passphrase for a symmetrical encrypted message."
    __slots__ = ()

class DECRYPTION_OKAY(namedtuple('DECRYPTION_OKAY', '')):
    msg = "The decryption process succeeded."
    __slots__ = ()

class NO_PUBKEY(namedtuple('NO_PUBKEY', 'long_keyid')):
    msg = "The key is not available"
    __slots__ = ()

class NO_SECKEY(namedtuple('NO_SECKEY', 'long_keyid')):
    msg = "The key is not available"
    __slots__ = ()

class IMPORT_CHECK(namedtuple('IMPORT_CHECK', ['long_keyid', 'fingerprint', 'user_ID'])):
    msg = 'This status is emitted in interactive mode right before the "import.okay" prompt.'
    __slots__ = ()

class IMPORTED(namedtuple('IMPORTED', ['long_keyid', 'username'])):
    msg = "The keyid and name of the signature just imported"
    __slots__ = ()

class IMPORT_OK(namedtuple('IMPORT_OK', ['reason', 'fingerprint'])):
    msg = \
"""The key with the primary key's FINGERPRINT has been imported.
    Reason flags:
      0 := Not actually changed
      1 := Entirely new key.
      2 := New user IDs
      4 := New signatures
      8 := New subkeys
     16 := Contains private key.
    The flags may be ORed."""
    __slots__ = ()

class IMPORT_PROBLEM(namedtuple('IMPORT_PROBLEM', ['reason', 'fingerprint'])):
    msg =  \
"""Issued for each import failure.  Reason codes are:
      0 := "No specific reason given".
      1 := "Invalid Certificate".
      2 := "Issuer Certificate missing".
      3 := "Certificate Chain too long".
      4 := "Error storing certificate"."""
    __slots__ = ()

class IMPORT_RES(namedtuple('IMPORT_RES', ['count', 'no_user_id', 'imported',
        'imported_rsa', 'unchanged', 'n_uids', 'n_subk', 'n_sigs',
        'n_revoc', 'sec_read', 'sec_imported', 'sec_dups',
        'skipped_new_keys', 'not_imported'])):
    msg = "Final statistics on import process."
    __slots__ = ()

class FILE_START(namedtuple('FILE_START', ['what', 'filename'])):
    msg = \
"""Start processing a file <filename>.
    <what> indicates the performed operation:
        1 - verify
        2 - encrypt
        3 - decrypt"""
    __slots__ = ()

class FILE_DONE(namedtuple('FILE_DONE', '')):
    msg = "Marks the end of a file processing which has been started by FILE_START."
    __slots__ = ()

class BEGIN_DECRYPTION(namedtuple('BEGIN_DECRYPTION', '')):
    msg = \
"""Mark the start of the actual decryption process.
These are also emitted when in --list-only mode."""
    __slots__ = ()

class END_DECRYPTION(namedtuple('END_DECRYPTION', '')):
    msg = \
"""Mark the end of the actual decryption process.
These are also emitted when in --list-only mode."""
    __slots__ = ()

class BEGIN_ENCRYPTION(namedtuple('BEGIN_ENCRYPTION', ['mdc_method', 'sym_algo'])):
    msg = "Mark the start of the actual encryption process."
    __slots__ = ()

class END_ENCRYPTION(namedtuple('END_ENCRYPTION', '')):
    msg = "Mark the end of the actual encryption process."
    __slots__ = ()

class BEGIN_SIGNING(namedtuple('BEGIN_SIGNING', 'hash_algo')):
    msg = "Mark the start of the actual signing process."

    __slots__ = ()

class DELETE_PROBLEM(namedtuple('DELETE_PROBLEM', 'reason_code')):
    msg = \
"""Deleting a key failed. Reason codes are:
        1 - No such key
        2 - Must delete secret key first
        3 - Ambigious specification"""
    __slots__ = ()

class PROGRESS(namedtuple('PROGRESS', ['what', 'char', 'cur', 'total'])):
    msg = \
"""Used by the primegen and Public key functions to indicate progress.
"char" is the character displayed with no --status-fd enabled, with
    the linefeed replaced by an 'X'.  "cur" is the current amount
    done and "total" is amount to be done; a "total" of 0 indicates that
    the total amount is not known.  The condition TOATL && CUR == TOTAL
    may be used to detect the end of an operation.
    Well known values for WHAT:
        "pk_dsa"   - DSA key generation
        "pk_elg"   - Elgamal key generation
        "primegen" - Prime generation
        "need_entropy" - Waiting for new entropy in the RNG
        "file:XXX" - processing file XXX
                     (note that current gpg versions leave out the
                     "file:" prefix).
        "tick"     - generic tick without any special meaning - useful
                     for letting clients know that the server is
                     still working.
        "starting_agent" - A gpg-agent was started because it is
                           not running as a daemon.
        "learncard" Send by the agent and gpgsm while learing
                    the data of a smartcard.
        "card_busy" A smartcard is still working"""
    __slots__ = ()

class SIG_CREATED(namedtuple('SIG_CREATED', ['type', 'pubkey_algo', 'hash_algo',
            'sig_class', 'timestamp', 'key_fpr'])):
    msg = \
"""A signature has been created using these parameters.
    type:  'D' = detached
           'C' = cleartext
           'S' = standard
           (only the first character should be checked)
   class:  2 hex digits with the signature class"""
    __slots__ = ()

class KEY_CREATED(namedtuple('KEY_CREATED', ['type', 'fingerprint', 'handle'])):
    msg = \
"""A key has been created
    type: 'B' = primary and subkey
          'P' = primary
          'S' = subkey"""
    __slots__ = ()

class KEY_NOT_CREATED(namedtuple('KEY_NOT_CREATED', 'handle')):
    msg = "The key from batch run has not been created due to errors."
    __slots__ = ()

class SESSION_KEY(namedtuple('SESSION_KEY', ['algo', 'hexdigits'])):
    msg = "The session key used to decrypt the message."
    __slots__ = ()

class NOTATION_NAM(namedtuple('NOTATION_NAME', 'name')):
    msg = "name and string are %XX escaped; the data may be split among several NOTATION_DATA lines."
    __slots__ = ()

class NOTATION_DATA(namedtuple('NOTATION_DATA', 'string')):
    msg = "Data assoiciated with the preceeding 'NOTATION_NAME'"
    __slots__ = ()

class USERID_HINT(namedtuple('USERID_HINT', ['long_main_keyid', 'string'])):
    msg = "Give a hint about the user ID for a certain keyID."
    __slots__ = ()

class POLICY_URL(namedtuple('POLICY_URL', 'string')):
    msg = ""
    __slots__ = ()

class BEGIN_STREAM(namedtuple('BEGIN_STREAM', '')):
    msg = "Issued by pipemode."
    __slots__ = ()

class END_STREAM(namedtuple('END_STREAM', '')):
    msg = "Issued by pipemode."
    __slots__ = ()

class INV_RECP(namedtuple('INV_RECP', ['reason', 'requested_recipient'])):
    msg = \
"""Issued for each unusable recipient/sender.
The reasons codes currently in use are:
    0 := "No specific reason given".
    1 := "Not Found"
    2 := "Ambigious specification"
    3 := "Wrong key usage"
    4 := "Key revoked"
    5 := "Key expired"
    6 := "No CRL known"
    7 := "CRL too old"
    8 := "Policy mismatch"
    9 := "Not a secret key"
    10 := "Key not trusted"
    11 := "Missing certificate"
    12 := "Missing issuer certificate"""
    __slots__ = ()

class INV_SGNR(namedtuple('INV_SGNR', ['reason', 'requested_sender'])):
    msg = \
"""Issued for each unusable recipient/sender.
The reasons codes currently in use are:
    0 := "No specific reason given".
    1 := "Not Found"
    2 := "Ambigious specification"
    3 := "Wrong key usage"
    4 := "Key revoked"
    5 := "Key expired"
    6 := "No CRL known"
    7 := "CRL too old"
    8 := "Policy mismatch"
    9 := "Not a secret key"
    10 := "Key not trusted"
    11 := "Missing certificate"
    12 := "Missing issuer certificate"""
    __slots__ = ()

class NO_RECP(namedtuple('NO_RECP', 'reserved')):
    msg = "Issued when no recipients are usable."
    __slots__ = ()

class NO_SGNR(namedtuple('NO_SGNR', 'reserved')):
    msg = "Issued when no senders are usable."
    __slots__ = ()

class ALREADY_SIGNED(namedtuple('ALREADY_SIGNED', 'long_keyid')):
    msg = "Warning: This is experimental and might be removed at any time."
    __slots__ = ()

class TRUNCATED(namedtuple('TRUNCATED', 'maxno')):
    msg = "The output was truncated to MAXNO items."
    __slots__ = ()

class ERROR(namedtuple('ERROR', ['error_location', 'error_code', 'more'])):
    msg = "This is a generic error status message, it might be followed by error location specific data."
    __slots__ = ()

class SUCCESS(namedtuple('SUCCESS', 'location')):
    msg = "Postive confirimation that an operation succeeded."
    __slots__ = ()

class ATTRIBUTE(namedtuple('ATTRIBUTE', ['fpr', 'octets', 'type', 'index', 'count',
            'timestamp', 'expiredate', 'flags'])):
    msg = "This is one long line issued for each attribute subpacket when an attribute packet is seen during key listing."
    __slots__ = ()

class CARDCTRL(namedtuple('CARDCTRL', ['what', 'serialno'])):
    msg = \
"""This is used to control smartcard operations.
    Defined values for WHAT are:
        1 = Request insertion of a card.  Serialnumber may be given
            to request a specific card.  Used by gpg 1.4 w/o scdaemon.
        2 = Request removal of a card.  Used by gpg 1.4 w/o scdaemon.
        3 = Card with serialnumber detected
        4 = No card available.
        5 = No card reader available
        6 = No card support available"""
    __slots__ = ()

class PLAINTEXT(namedtuple('PLAINTEXT', ['format', 'timestamp', 'filename'])):
    msg = "This indicates the format of the plaintext that is about to be written."
    __slots__ = ()

class PLAINTEXT_LENGTH(namedtuple('PLAINTEXT_LENGTH', 'length')):
    msg = "This indicates the length of the plaintext that is about to be written."
    __slots__ = ()

class SIG_SUBPACKET(namedtuple('SIG_SUBPACKET', ['type', 'flags', 'length', 'data'])):
    msg = "This indicates that a signature subpacket was seen."
    __slots__ = ()

class SC_OP_FAILURE(namedtuple('SC_OP_FAILURE', 'code')):
    msg = \
"""An operation on a smartcard definitely failed.
    Defined values for CODE are:
        0 - unspecified error (identically to a missing CODE)
        1 - canceled
        2 - bad PIN"""
    __slots__ = ()

class SC_OP_SUCCESS(namedtuple('SC_OP_SUCCESS', '')):
    msg = "A smart card operaion succeeded."
    __slots__ = ()

class BACKUP_KEY_CREATED(namedtuple('BACKUP_KEY_CREATED', ['fingerprint', 'fname'])):
    msg = "A backup key named FNAME has been created for the key with KEYID."
    __slots__ = ()

class MOUNTPOINT(namedtuple('MOUNTPOINT', 'name')):
    msg = "NAME is a percent-plus escaped filename describing the mountpoint for the current operation (e.g. g13 --mount)."
    __slots__ = ()

class DECRYPTION_INFO(namedtuple('DECRYPTION_INFO', ['mdc_method', 'sym_algo'])):
    msg = "Print information about the symmetric encryption algorithm and the MDC method."
