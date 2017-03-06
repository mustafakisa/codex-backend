# Copyright (C) 2016 Deloitte Argentina.
# This file is part of CodexGigas - https://github.com/codexgigassys/
# See the file 'LICENSE' for copying permission.

tree_element = {"name": "Portable Executable", "children": [
    {"name": "File entropy", "id": 6, "type": "string", "children": [], "searchable":True, "projectable":True, "call_func": ""},
    {"name": "Packer detection", "id": 7, "type": "checkbox", "children": [], "searchable":True, "projectable":True, "call_func": ""},
    {"name": "Imports", "children": [
        {"name": "Function", "id": 8, "type": "string", "example": "getprocaddress", "multi": True, "children": [], "searchable":True, "projectable":False, "call_func": "check_imp", "lower": True},
        {"name": "Library", "id": 9, "type": "string", "example": "kernel32.dll", "multi": True, "children": [], "searchable":True, "projectable":False, "call_func": "check_lib", "lower": True},
        {"name": "Hidden Function", "id": 100, "type": "string", "example": "getprocaddress", "multi": True, "children": [], "searchable":True, "projectable":False, "call_func": "check_imp", "lower": True},
        {"name": "Hidden Library", "id": 101, "type": "string", "example": "kernel32.dll", "multi": True, "children": [], "searchable":True, "projectable":False, "call_func": "check_lib", "lower": True}
    ]},
    {"name": "Sections", "children": [
        {"name": "Section Hash", "id": 12, "type": "string", "example": "72c0e35b5ae8124264f3694331f843a2", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Section name", "id": 15, "type": "string", "example": ".text\\x00\\x00\\x00", "children": [], "searchable":True, "projectable":False, "call_func": "", "lower": False},
        {"name": "Section size of RAW data", "id": 16, "type": "number", "example": "78336", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Section virtual size", "id": 17, "type": "number", "example": "81920", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        # {"name":"Section characteristics","id":18,"type":"string","example":"0xe0000020","children":[],"searchable":True,"projectable":False},
        {"name": "Section entropy", "id": 19, "type": "string", "example": "7.9886263288849335", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Section write executable", "id": 20, "type": "checkbox", "example": "True", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        # {"name":"Section fast fuzzy","id":21,"type":"string","example":"Not Implemented","children":[],"searchable":True,"projectable":False}
    ]},
    {"name": "Headers", "children": [
        {"name": "Optional header", "children": [
            {"name": "Dll characteristics", "id": 22, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Base of code", "id": 23, "type": "string", "example": "0x1000", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Major linker version", "id": 24, "type": "string", "example": "0x6", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Minor operating System version", "id": 25, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Major subsystem version", "id": 26, "type": "string", "example": "0x4", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Loader flags", "id": 27, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Size of stack commit", "id": 28, "type": "string", "example": "0x1000", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Size of unitialized data", "id": 29, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Minor subsystem version", "id": 30, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Size of heap reserve", "id": 31, "type": "string", "example": "0x100000", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Size of heap commit", "id": 32, "type": "string", "example": "0x1000", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Size of starck reserve", "id": 33, "type": "string", "example": "0x100000", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Size of headers", "id": 34, "type": "string", "example": "0x200", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Section alignment", "id": 35, "type": "string", "example": "0x1000", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Optional magic", "id": 36, "type": "string", "example": "0x10b", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Minor image version", "id": 37, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Major image version", "id": 38, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File alignment", "id": 39, "type": "string", "example": "0x200", "example": "",  "children": [], "searchable":True, "projectable":True},
            {"name": "Major operating system version", "id": 40, "type": "string", "example": "0x4", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Address of entry point", "id": 41, "type": "string", "example": "0x1040", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Subsystem", "id": 42, "type": "string", "example": "0x2", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Size of code", "id": 43, "type": "string", "example": "0x200", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Image base", "id": 44, "type": "string", "example": "0x400000", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Size of initialized data", "id": 45, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Size of image", "id": 46, "type": "string", "example": "0x15000", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Number of RVA and sizes", "id": 47, "type": "string", "example": "0x10", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Checksum", "id": 48, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Reserverd1", "id": 49, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Minor linker version", "id": 50, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""}
        ]},
        {"name": "Dos header", "children": [
            {"name": "OEM identifier", "id": 51, "type": "string", "example": "0x10b", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Dos magic", "id": 52, "type": "string", "example": "0x5ad", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Initial SS value", "id": 53, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Initial IP value", "id": 54, "type": "string", "example": "0x7279", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Initial SP value", "id": 55, "type": "string", "example": "0x14c", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File addr of new exe header", "id": 56, "type": "string", "example": "0xc", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File addr of relocation table", "id": 57, "type": "string", "example": "0x4c5b", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Relocations", "id": 58, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Reserved words 2", "id": 59, "type": "string", "example": "\\x00\\x02\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00@\\x10\\x00\\x00\\x00\\x10\\x00\\x00", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Min extra paragraphs needed", "id": 60, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "OEM information", "id": 61, "type": "string", "example": "0x6", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Overlay number", "id": 62, "type": "string", "example": "0x726f", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Reserved words 1", "id": 63, "type": "string", "example": "dPE]\\xe0\\x00\\x0f\\x01", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Checksum", "id": 64, "type": "string", "example": "0x1", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Pages in file", "id": 65, "type": "string", "example": "0x3", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Bytes on last page of file", "id": 66, "type": "string", "example": "0x90", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Max extra paragraphs needed", "id": 67, "type": "string", "example": "0x445", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Initial CS value", "id": 68, "type": "string", "example": "0x3c66", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Size of header in paragraphs", "id": 69, "type": "string", "example": "0x4", "children": [], "searchable":True, "projectable":True, "call_func": ""}
        ]},
        {"name": "NT header", "children": [
            {"name": "Signature", "id": 70, "type": "string", "example": "0x4550", "children": [], "searchable":True, "projectable":True, "call_func": ""}
        ]},
        {"name": "File header", "children": [
            {"name": "Time date stamp", "id": 71, "type": "string", "example": "0x3c667279", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Characteristics", "id": 72, "type": "string", "example": "0x10f", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Pointer to symbol table", "id": 73, "type": "string", "example": "0x726f4c5b", "children": [], "searchable":True, "projectable":True},
            {"name": "Machine", "id": 74, "type": "string", "example": "0x14c", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Size of optional header", "id": 75, "type": "string", "example": "0xe0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Number of sections", "id": 76, "type": "string", "example": "0x1", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Number of symbols", "id": 77, "type": "string", "example": "0x5d455064", "children": [], "searchable":True, "projectable":True, "call_func": ""}
        ]}
    ]},
    {"name": "Resource Entries", "children": [
        {"name": "Resource language", "id": 78, "type": "string", "example": "LANG_NEUTRAL", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Resource RVA", "id": 79, "type": "string", "example": "0x2a238", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Resource SHA1", "id": 80, "type": "string", "example": "4a784ea5583b9fba41c0303ece802671844d2f5d", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Resource name", "id": 81, "type": "string", "example": "RT_ICON", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Resource sublanguage", "id": 82, "type": "string", "example": "SUBLANG_NEUTRAL", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Resource size", "id": 83, "type": "string", "example": "0x468", "children": [], "searchable":True, "projectable":False, "call_func": ""}
    ]},
    {"name": "Version", "children": [
        {"name": "Fixed File Info", "children": [
            {"name": "Product version MS", "id": 84, "type": "string", "example": "0x30001", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File flags mask", "id": 85, "type": "string", "example": "0x17", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File type", "id": 86, "type": "string", "example": "0x1", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File version MS", "id": 87, "type": "string", "example": "0x30001", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File version LS", "id": 88, "type": "string", "example": "0x40000", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File subtype", "id": 89, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File flags", "id": 90, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File date LS", "id": 91, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Product version LS", "id": 92, "type": "string", "example": "0x10000", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Signature", "id": 93, "type": "string", "example": "0xfeef04bd", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File date MS", "id": 94, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "File OS", "id": 95, "type": "string", "example": "0x4", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Struc version", "id": 96, "type": "string", "example": "0x10000", "children": [], "searchable":True, "projectable":True, "call_func": ""}
        ]},
        {"name": "Version Info", "children": [
            {"name": "Version value lenght", "id": 97, "type": "string", "example": "0x34", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version Length", "id": 98, "type": "string", "example": "0x298", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version Type", "id": 99, "type": "string", "example": "0x0", "children": [], "searchable":True, "projectable":True, "call_func": ""}
        ]},
        {"name": "Version String", "children": [
            {"name": "Version String LangID", "id": 124, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String LegalCopyright", "id": 125, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String InternalName", "id": 126, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String FileVersion", "id": 127, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String CompanyName", "id": 128, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String ProductName", "id": 129, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String ProductVersion", "id": 130, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String FileDescription", "id": 131, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String OriginalFilename", "id": 132, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String Comments", "id": 133, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String LegalTrademarks", "id": 134, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String PrivateBuild", "id": 135, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
            {"name": "Version String SpecialBuild", "id": 136, "type": "string", "example": "", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        ]},
    ]},
    {"name": "Strings", "children": [
        {"name": "Emails", "id": 102, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "URLs", "id": 103, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "IPs", "id": 104, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Domains", "id": 105, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Interesting", "id": 106, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": "", "multi": True},
        {"name": "Registrys", "id": 107, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""}
    ]},
    {"name": "Exports", "children": [
        {"name": "Exports Characteristics", "id": 108, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Exports Time Date Stamp", "id": 109, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Exports Major Version", "id": 110, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Exports Minor Version", "id": 111, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Exports Name", "id": 112, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Exports Base", "id": 113, "type": "number", "children": [], "searchable":True, "projectable":True},
        {"name": "Exports Number Of Functions", "id": 114, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Exports Number Of Names", "id": 115, "type": "number", "children": [], "searchable":True, "projectable":True},
        {"name": "Exports Address Of Functions", "id": 116, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Exports Address Of Names", "id": 117, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Exports Address Of Ordinals", "id": 118, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Exported Symbols", "children": [
            {"name": "Symbol Ordinal", "id": 119, "type": "number", "children": [], "searchable":True, "projectable":False, "call_func": ""},
            {"name": "Symbol Name", "id": 120, "type": "string", "example": "getprocaddress", "children": [], "searchable":True, "projectable":False, "call_func": "", "multi": True},
            {"name": "Symbol RVA", "id": 121, "type": "number", "children": [], "searchable":True, "projectable":False, "call_func": ""},
            {"name": "Symbol Forwarder DLL", "id": 122, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""},
            {"name": "Symbol Forwarder Function", "id": 123, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        ]}
    ]},
    {"name": "Certificates", "children": [
        {"name": "Certificate Length", "id": 137, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Certificate Revision", "id": 138, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Certificate Type", "id": 139, "type": "number", "children": [], "searchable":True, "projectable":True, "call_func": ""},
        {"name": "Certificate Serial Number", "id": 140, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Certificate Issuer", "id": 141, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Certificate Subject", "id": 142, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Certificate Validity Begin", "id": 143, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Certificate Validity End", "id": 144, "type": "string", "children": [], "searchable":True, "projectable":False, "call_func": ""},
        {"name": "Certificate Signed", "id": 145, "type": "checkbox", "children": [], "searchable":True, "projectable":True, "call_func": ""},
    ]}
]}

id_element = {
    6: {"path": "particular_header.file_entropy", "type": "float"},
    7: {"path": "particular_header.packer_detection", "type": "check"},
    8: {"path": "particular_header.imports.functions", "type": "s_string"},
    9: {"path": "particular_header.imports.lib", "type": "s_string"},
    12: {"path": "particular_header.sections.md5", "type": "string", "do": "clean_hash"},
    13: {"path": "particular_header.sections.sha1", "type": "string", "do": "clean_hash"},
    14: {"path": "particular_header.sections.sha2", "type": "string", "do": "clean_hash"},
    15: {"path": "particular_header.sections.name", "type": "s_string_no_lower"},
    16: {"path": "particular_header.sections.size_raw_data", "type": "int"},
    17: {"path": "particular_header.sections.virtual_size", "type": "int"},
    18: {"path": "particular_header.sections.characteristics", "type": "string"},
    19: {"path": "particular_header.sections.entropy", "type": "float"},
    20: {"path": "particular_header.sections.write_executable", "type": "check"},
    21: {},
    22: {"path": "particular_header.headers.optional_header.DllCharacteristics", "type": "s_string"},
    23: {"path": "particular_header.headers.optional_header.BaseOfCode", "type": "s_string"},
    24: {"path": "particular_header.headers.optional_header.MajorLinkerVersion", "type": "s_string"},
    25: {"path": "particular_header.headers.optional_header.MinorOperatingSystemVersion", "type": "s_string"},
    26: {"path": "particular_header.headers.optional_header.MajorSubsystemVersion", "type": "s_string"},
    27: {"path": "particular_header.headers.optional_header.LoaderFlags", "type": "s_string"},
    28: {"path": "particular_header.headers.optional_header.SizeOfStackCommit", "type": "s_string"},
    29: {"path": "particular_header.headers.optional_header.SizeOfUninitializedData", "type": "s_string"},
    30: {"path": "particular_header.headers.optional_header.MinorSubsystemVersion", "type": "s_string"},
    31: {"path": "particular_header.headers.optional_header.SizeOfHeapReserve", "type": "s_string"},
    32: {"path": "particular_header.headers.optional_header.SizeOfHeapCommit", "type": "s_string"},
    33: {"path": "particular_header.headers.optional_header.SizeOfStackReserve", "type": "s_string"},
    34: {"path": "particular_header.headers.optional_header.SizeOfHeaders", "type": "s_string"},
    35: {"path": "particular_header.headers.optional_header.SectionAlignment", "type": "s_string"},
    36: {"path": "particular_header.headers.optional_header.Magic", "type": "s_string"},
    37: {"path": "particular_header.headers.optional_header.MinorImageVersion", "type": "s_string"},
    38: {"path": "particular_header.headers.optional_header.MajorImageVersion", "type": "s_string"},
    39: {"path": "particular_header.headers.optional_header.FileAlignment", "type": "s_string"},
    40: {"path": "particular_header.headers.optional_header.MajorOperatingSystemVersion", "type": "s_string"},
    41: {"path": "particular_header.headers.optional_header.AddressOfEntryPoint", "type": "s_string"},
    42: {"path": "particular_header.headers.optional_header.Subsystem", "type": "s_string"},
    43: {"path": "particular_header.headers.optional_header.SizeOfCode", "type": "s_string"},
    44: {"path": "particular_header.headers.optional_header.ImageBase", "type": "s_string"},
    45: {"path": "particular_header.headers.optional_header.SizeOfInitializedData", "type": "s_string"},
    46: {"path": "particular_header.headers.optional_header.SizeOfImage", "type": "s_string"},
    47: {"path": "particular_header.headers.optional_header.NumberOfRvaAndSizes", "type": "s_string"},
    48: {"path": "particular_header.headers.optional_header.CheckSum", "type": "s_string"},
    49: {"path": "particular_header.headers.optional_header.Reserved1", "type": "s_string"},
    50: {"path": "particular_header.headers.optional_header.MinorLinkerVersion", "type": "s_string"},
    51: {"path": "particular_header.headers.dos_header.oemid", "type": "s_string"},
    52: {"path": "particular_header.headers.dos_header.magic", "type": "s_string"},
    53: {"path": "particular_header.headers.dos_header.ss", "type": "s_string"},
    54: {"path": "particular_header.headers.dos_header.ip", "type": "s_string"},
    55: {"path": "particular_header.headers.dos_header.sp", "type": "s_string"},
    56: {"path": "particular_header.headers.dos_header.lfanew", "type": "s_string"},
    57: {"path": "particular_header.headers.dos_header.lfarlc", "type": "s_string"},
    58: {"path": "particular_header.headers.dos_header.crlc", "type": "s_string"},
    59: {"path": "particular_header.headers.dos_header.res2", "type": "s_string"},
    60: {"path": "particular_header.headers.dos_header.minalloc", "type": "s_string"},
    61: {"path": "particular_header.headers.dos_header.oeminfo", "type": "s_string"},
    62: {"path": "particular_header.headers.dos_header.ovno", "type": "s_string"},
    63: {"path": "particular_header.headers.dos_header.res", "type": "s_string_nl"},
    64: {"path": "particular_header.headers.dos_header.csum", "type": "s_string"},
    65: {"path": "particular_header.headers.dos_header.cp", "type": "s_string"},
    66: {"path": "particular_header.headers.dos_header.cblp", "type": "s_string"},
    67: {"path": "particular_header.headers.dos_header.maxalloc", "type": "s_string"},
    68: {"path": "particular_header.headers.dos_header.cs", "type": "s_string"},
    69: {"path": "particular_header.headers.dos_header.cparhdr", "type": "s_string"},
    70: {"path": "particular_header.headers.nt_header.Signature", "type": "s_string"},
    71: {"path": "particular_header.headers.file_header.TimeDateStamp", "type": "s_string"},
    72: {"path": "particular_header.headers.file_header.Characteristics", "type": "s_string"},
    73: {"path": "particular_header.headers.file_header.PointerToSymbolTable", "type": "s_string"},
    74: {"path": "particular_header.headers.file_header.Machine", "type": "s_string"},
    75: {"path": "particular_header.headers.file_header.SizeOfOptionalHeader", "type": "s_string"},
    76: {"path": "particular_header.headers.file_header.NumberOfSections", "type": "s_string"},
    77: {"path": "particular_header.headers.file_header.NumberOfSymbols", "type": "s_string"},
    78: {"path": "particular_header.res_entries.lang", "type": "s_string_nl"},
    79: {"path": "particular_header.res_entries.rva", "type": "s_string"},
    80: {"path": "particular_header.res_entries.sha1", "type": "string"},
    81: {"path": "particular_header.res_entries.name", "type": "s_string_nl"},
    82: {"path": "particular_header.res_entries.sublang", "type": "s_string_nl"},
    83: {"path": "particular_header.res_entries.size", "type": "s_string"},
    84: {"path": "particular_header.version.fixed_file_info.ProductVersionMS", "type": "s_string"},
    85: {"path": "particular_header.version.fixed_file_info.FileFlagsMask", "type": "s_string"},
    86: {"path": "particular_header.version.fixed_file_info.FileType", "type": "s_string"},
    87: {"path": "particular_header.version.fixed_file_info.FileVersionMS", "type": "s_string"},
    88: {"path": "particular_header.version.fixed_file_info.FileVersionLS", "type": "s_string"},
    89: {"path": "particular_header.version.fixed_file_info.FileSubtype", "type": "s_string"},
    90: {"path": "particular_header.version.fixed_file_info.FileFlags", "type": "s_string"},
    91: {"path": "particular_header.version.fixed_file_info.FileDateLS", "type": "s_string"},
    92: {"path": "particular_header.version.fixed_file_info.ProductVersionLS", "type": "s_string"},
    93: {"path": "particular_header.version.fixed_file_info.Signature", "type": "s_string"},
    94: {"path": "particular_header.version.fixed_file_info.FileDateMS", "type": "s_string"},
    95: {"path": "particular_header.version.fixed_file_info.FileOS", "type": "s_string"},
    96: {"path": "particular_header.version.fixed_file_info.StrucVersion", "type": "s_string"},
    97: {"path": "particular_header.version.version_info.ValueLength", "type": "s_string"},
    98: {"path": "particular_header.version.version_info.Length", "type": "s_string"},
    99: {"path": "particular_header.version.version_info.Type", "type": "s_string"},
    100: {"path": "particular_header.strings.hidden_imports", "type": "s_string"},
    101: {"path": "particular_header.strings.hidden_dll", "type": "s_string"},
    102: {"path": "particular_header.strings.emails", "type": "s_string"},
    103: {"path": "particular_header.strings.urls", "type": "s_string"},
    104: {"path": "particular_header.strings.ips", "type": "s_string"},
    105: {"path": "particular_header.strings.domains", "type": "s_string"},
    106: {"path": "particular_header.strings.interesting", "type": "s_string"},
    107: {"path": "particular_header.strings.registry", "type": "s_string"},
    108: {"path": "particular_header.exports.characteristics", "type": "int"},
    109: {"path": "particular_header.exports.timeDateStamp", "type": "int"},
    110: {"path": "particular_header.exports.majorVersion", "type": "int"},
    111: {"path": "particular_header.exports.minorVersion", "type": "int"},
    112: {"path": "particular_header.exports.name", "type": "int"},
    113: {"path": "particular_header.exports.base", "type": "int"},
    114: {"path": "particular_header.exports.numberOfFunctions", "type": "int"},
    115: {"path": "particular_header.exports.numberOfNames", "type": "int"},
    116: {"path": "particular_header.exports.addressOfFunctions", "type": "int"},
    117: {"path": "particular_header.exports.AddressOfNames", "type": "int"},
    118: {"path": "particular_header.exports.AddressOfOrdinals", "type": "int"},
    119: {"path": "particular_header.exports.symbols.ordinal", "type": "int"},
    120: {"path": "particular_header.exports.symbols.name", "type": "string"},
    121: {"path": "particular_header.exports.symbols.RVA", "type": "int"},
    122: {"path": "particular_header.exports.symbols.forwarder_dll", "type": "string"},
    123: {"path": "particular_header.exports.symbols.forwarder_function", "type": "string"},
    124: {"path": "particular_header.version.string_file_info.LangID", "type": "string"},
    125: {"path": "particular_header.version.string_file_info.LegalCopyright", "type": "string"},
    126: {"path": "particular_header.version.string_file_info.InternalName", "type": "string"},
    127: {"path": "particular_header.version.string_file_info.FileVersion", "type": "string"},
    128: {"path": "particular_header.version.string_file_info.CompanyName", "type": "string"},
    129: {"path": "particular_header.version.string_file_info.ProductName", "type": "string"},
    130: {"path": "particular_header.version.string_file_info.ProductVersion", "type": "string"},
    131: {"path": "particular_header.version.string_file_info.FileDescription", "type": "string"},
    132: {"path": "particular_header.version.string_file_info.OriginalFilename", "type": "string"},
    133: {"path": "particular_header.version.string_file_info.Comments", "type": "string"},
    134: {"path": "particular_header.version.string_file_info.LegalTrademarks", "type": "string"},
    135: {"path": "particular_header.version.string_file_info.PrivateBuild", "type": "string"},
    136: {"path": "particular_header.version.string_file_info.SpecialBuild", "type": "string"},
    137: {"path": "particular_header.certificate.length", "type": "int"},
    138: {"path": "particular_header.certificate.revision", "type": "int"},
    139: {"path": "particular_header.certificate.type", "type": "int"},
    140: {"path": "particular_header.certificate.certificates.serial", "type": "string"},
    141: {"path": "particular_header.certificate.certificates.issuer", "type": "string"},
    142: {"path": "particular_header.certificate.certificates.subject", "type": "string"},
    143: {"path": "particular_header.certificate.certificates.validity_beg", "type": "string"},
    144: {"path": "particular_header.certificate.certificates.validity_end", "type": "string"},
    145: {"path": "particular_header.certificate.signed", "type": "check"}
}
