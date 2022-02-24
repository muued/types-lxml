# Hand-written stub for lxml.etree as used by mypy.report.
# This is *far* from complete, and the stubgen-generated ones crash mypy.
# Any use of `Any` below means I couldn't figure out the type.

from typing import (
    IO,
    Any,
    Callable,
    Collection,
    Dict,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Reversible,
    Sequence,
    SupportsBytes,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from typing_extensions import Literal, Protocol, TypeGuard

from .._types import (
    SupportsLaxedItems,
    _AnyStr,
    _Dict_Tuple2AnyStr_Any,
    _DictAnyStr,
    _ListAnyStr,
    _NonDefaultNSMapArg,
    _NSMapArg,
    _XPathObject,
    _XPathVarArg,
)
from ..cssselect import _CSSTransArg
from ._xmlerror import (
    ErrorDomains as ErrorDomains,
    ErrorLevels as ErrorLevels,
    ErrorTypes as ErrorTypes,
    PyErrorLog as PyErrorLog,
    RelaxNGErrorTypes as RelaxNGErrorTypes,
    _BaseErrorLog,
    _ErrorLog,
    clear_error_log as clear_error_log,
    use_global_python_log as use_global_python_log,
)
from ._xpath import (
    ETXPath as ETXPath,
    XPath as XPath,
    XPathDocumentEvaluator as XPathDocumentEvaluator,
    XPathElementEvaluator as XPathElementEvaluator,
    XPathError as XPathError,
    XPathEvaluator as XPathEvaluator,
    XPathSyntaxError as XPathSyntaxError,
)

#
# Basic variables and constants
#

_TagName = Union[str, bytes, QName]
# Note that _TagSelector filters element type not by classes, but
# checks for element _factory functions_ instead
# (that is Element(), Comment() and ProcessingInstruction()).
# Unrealistic to explicitly union callables of different arguments.
_TagSelector = Union[str, bytes, QName, Callable[..., _Element]]
_T = TypeVar("_T")
_KnownEncodings = Literal[
    "ASCII",
    "ascii",
    "UTF-8",
    "utf-8",
    "UTF8",
    "utf8",
    "US-ASCII",
    "us-ascii",
]
_ElementOrTree = Union[_Element, _ElementTree]

class _SmartStr(str):
    """Smart string is a private str subclass documented in
    [return types](https://lxml.de/xpathxslt.html#xpath-return-values)
    of XPath evaluation result. This stub-only class can be utilized like:

    ```python
    if TYPE_CHECKING:
        from lxml.etree import _SmartStr
    def is_smart_str(s: str) -> TypeGuard[_SmartStr]:
        return hasattr(s, 'getparent')
    if is_smart_str(result):
        parent = result.getparent() # identified as lxml.etree._Element
    ```
    """

    is_attribute: bool
    is_tail: bool
    is_text: bool
    attrname: Optional[str]
    def getparent(self) -> Optional[_Element]: ...

class DocInfo:
    root_name = ...  # type: str
    public_id = ...  # type: Optional[str]
    system_id = ...  # type: Optional[str]
    xml_version = ...  # type: Optional[str]
    encoding = ...  # type: Optional[str]
    standalone = ...  # type: Optional[bool]
    URL = ...  # type: str
    internalDTD = ...  # type: "DTD"
    externalDTD = ...  # type: "DTD"
    def __init__(self, tree: Union["_ElementTree", "_Element"]) -> None: ...
    def clear(self) -> None: ...

# The base of _Element is *almost* an amalgam of MutableSequence[_Element]
# plus mixin methods for _Attrib.
# Extra methods follow the order of _Element source approximately
class _Element(Collection[_Element], Reversible[_Element]):
    #
    # Common properties
    #
    @property
    def tag(self) -> str: ...
    @tag.setter
    def tag(self, value: _TagName) -> None: ...
    @property
    def attrib(self) -> _Attrib: ...
    @property
    def text(self) -> str | None: ...
    @text.setter
    def text(self, value: Optional[_AnyStr | QName]) -> None: ...  # FIXME missing CDATA
    @property
    def tail(self) -> str | None: ...
    @tail.setter
    def tail(self, value: Optional[_AnyStr]) -> None: ...  # FIXME missing CDATA
    #
    # _Element-only properties
    # Following props are marked as read-only in comment,
    # but 'sourceline' and 'base' provide __set__ method
    # --- and they do work.
    #
    @property
    def prefix(self) -> str | None: ...
    @property
    def sourceline(self) -> int | None: ...
    @sourceline.setter
    def sourceline(self, value: int) -> None: ...
    @property
    def nsmap(self) -> dict[str | None, str]: ...
    @property
    def base(self) -> str | None: ...
    @base.setter
    def base(self, value: Optional[_AnyStr]) -> None: ...
    #
    # Accessors
    #
    def __delitem__(self, __k: int | slice) -> None: ...
    @overload
    def __getitem__(self, __x: int) -> _Element: ...
    @overload
    def __getitem__(self, __x: slice) -> list[_Element]: ...
    @overload
    def __setitem__(self, __x: int, __v: _Element) -> None: ...
    @overload
    def __setitem__(self, __x: slice, __v: Iterable[_Element]) -> None: ...
    def __contains__(self, __x: object) -> bool: ...
    def __len__(self) -> int: ...
    # There are a hoard of element iterators used in lxml, but
    # they only differ in implementation detail and don't affect typing.
    def __iter__(self) -> Iterator[_Element]: ...
    def __reversed__(self) -> Iterator[_Element]: ...
    def set(self, key: _TagName, value: _AnyStr) -> None: ...
    def append(self, element: _Element) -> None: ...
    def extend(self, elements: Iterable[_Element]) -> None: ...
    def clear(self, keep_tail: bool = ...) -> None: ...
    def insert(self, index: int, element: _Element) -> None: ...
    def remove(self, element: _Element) -> None: ...
    def index(
        self, child: _Element, start: int | None = ..., end: int | None = ...
    ) -> int: ...
    @overload
    def get(self, key: _TagName) -> str | None: ...
    @overload
    def get(self, key: _TagName, default: _T) -> str | _T: ...
    def keys(self) -> list[str]: ...
    def values(self) -> list[str]: ...
    def items(self) -> list[tuple[str, str]]: ...
    #
    # extra Element / ET methods
    #
    def addnext(self, element: _Element) -> None: ...
    def addprevious(self, element: _Element) -> None: ...
    def replace(self, old_element: _Element, new_element: _Element) -> None: ...
    def getparent(self) -> _Element | None: ...
    def getnext(self) -> _Element | None: ...
    def getprevious(self) -> _Element | None: ...
    def itersiblings(
        self,
        tag: Optional[_TagSelector] = ...,
        *tags: _TagSelector,
        preceding: bool = ...,
    ) -> Iterator[_Element]: ...
    def iterancestors(
        self, tag: Optional[_TagSelector] = ..., *tags: _TagSelector
    ) -> Iterator[_Element]: ...
    def iterdescendants(
        self, tag: Optional[_TagSelector] = ..., *tags: _TagSelector
    ) -> Iterator[_Element]: ...
    def iterchildren(
        self,
        tag: Optional[_TagSelector] = ...,
        *tags: _TagSelector,
        reversed: bool = ...,
    ) -> Iterator[_Element]: ...
    def getroottree(self) -> _ElementTree: ...
    def iter(
        self, tag: Optional[_TagSelector] = ..., *tags: _TagSelector
    ) -> Iterator[_Element]: ...
    def itertext(
        self,
        tag: Optional[_TagSelector] = ...,
        *tags: _TagSelector,
        with_tail: bool = ...,
    ) -> Iterator[str]: ...
    def makeelement(
        self,
        _tag: _TagName,
        # Final result is sort of like {**attrib, **_extra}
        attrib: SupportsLaxedItems[str, _AnyStr] | None = ...,
        nsmap: _NSMapArg = ...,
        **_extra: _AnyStr,
    ) -> _Element: ...
    # Elementpath API doesn't do str/byte conversion, only unicode accepted for py3
    def find(
        self, path: str | QName, namespaces: _NSMapArg = ...
    ) -> _Element | None: ...
    @overload
    def findtext(
        self,
        path: str | QName,
        namespaces: _NSMapArg = ...,
    ) -> str | None: ...
    @overload
    def findtext(
        self,
        path: str | QName,
        default: _T = ...,
        namespaces: _NSMapArg = ...,
    ) -> str | _T: ...
    def findall(
        self, path: str | QName, namespaces: _NSMapArg = ...
    ) -> list[_Element]: ...
    def iterfind(
        self, path: str | QName, namespaces: _NSMapArg = ...
    ) -> Iterator[_Element]: ...
    def xpath(
        self,
        _path: _AnyStr,
        namespaces: _NonDefaultNSMapArg = ...,
        extensions: Any = ...,
        smart_strings: bool = ...,
        **_variables: _XPathVarArg,
    ) -> _XPathObject: ...
    def cssselect(
        self,
        expression: str,
        *,
        translator: _CSSTransArg = ...,
    ) -> list[_Element]: ...
    # Following methods marked as deprecated upstream
    def getchildren(self) -> list[_Element]: ...  # = list(self)
    def getiterator(
        self,
        tag: Optional[_TagSelector],
        *tags: _TagSelector,
    ) -> Iterator[_Element]: ...

class ElementBase(_Element): ...

class _ElementTree:
    parser = ...  # type: XMLParser
    docinfo = ...  # type: DocInfo
    def find(self, path: str, namespaces: _NSMapArg = ...) -> Optional["_Element"]: ...
    def findtext(
        self,
        path: str,
        default: Optional[str] = ...,
        namespaces: _NSMapArg = ...,
    ) -> Optional[str]: ...
    def findall(self, path: str, namespaces: _NSMapArg = ...) -> List["_Element"]: ...
    def getpath(self, element: _Element) -> str: ...
    def getroot(self) -> _Element: ...
    def iter(
        self, tag: Optional[_TagSelector] = ..., *tags: _TagSelector
    ) -> Iterable[_Element]: ...
    def write(
        self,
        file: Union[_AnyStr, IO[Any]],
        encoding: _AnyStr = ...,
        method: _AnyStr = ...,
        pretty_print: bool = ...,
        xml_declaration: Any = ...,
        with_tail: Any = ...,
        standalone: bool = ...,
        compression: int = ...,
        exclusive: bool = ...,
        with_comments: bool = ...,
        inclusive_ns_prefixes: _ListAnyStr = ...,
    ) -> None: ...
    def write_c14n(
        self,
        file: Union[_AnyStr, IO[Any]],
        with_comments: bool = ...,
        compression: int = ...,
        inclusive_ns_prefixes: Iterable[_AnyStr] = ...,
    ) -> None: ...
    def _setroot(self, root: _Element) -> None: ...
    def xinclude(self) -> None: ...
    def xpath(
        self,
        _path: _AnyStr,
        namespaces: _NonDefaultNSMapArg = ...,
        extensions: Any = ...,
        smart_strings: bool = ...,
        **_variables: _XPathVarArg,
    ) -> _XPathObject: ...
    def xslt(
        self,
        _xslt: XSLT,
        extensions: Optional[_Dict_Tuple2AnyStr_Any] = ...,
        access_control: Optional[XSLTAccessControl] = ...,
        **_variables: Any,
    ) -> _ElementTree: ...

class __ContentOnlyElement(_Element): ...
class _Comment(__ContentOnlyElement): ...

class _ProcessingInstruction(__ContentOnlyElement):
    target: _AnyStr

class _Attrib:
    def __setitem__(self, key: _AnyStr, value: _AnyStr) -> None: ...
    def __delitem__(self, key: _AnyStr) -> None: ...
    def update(
        self,
        sequence_or_dict: Union[
            _Attrib, Mapping[_AnyStr, _AnyStr], Sequence[Tuple[_AnyStr, _AnyStr]]
        ],
    ) -> None: ...
    def pop(self, key: _AnyStr, default: _AnyStr) -> _AnyStr: ...
    def clear(self) -> None: ...
    def __repr__(self) -> str: ...
    def __copy__(self) -> _DictAnyStr: ...
    def __deepcopy__(self, memo: Dict[Any, Any]) -> _DictAnyStr: ...
    def __getitem__(self, key: _AnyStr) -> _AnyStr: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def get(self, key: _AnyStr, default: _AnyStr = ...) -> Optional[_AnyStr]: ...
    def keys(self) -> _ListAnyStr: ...
    def __iter__(self) -> Iterator[_AnyStr]: ...  # actually _AttribIterator
    def iterkeys(self) -> Iterator[_AnyStr]: ...
    def values(self) -> _ListAnyStr: ...
    def itervalues(self) -> Iterator[_AnyStr]: ...
    def items(self) -> List[Tuple[_AnyStr, _AnyStr]]: ...
    def iteritems(self) -> Iterator[Tuple[_AnyStr, _AnyStr]]: ...
    def has_key(self, key: _AnyStr) -> bool: ...
    def __contains__(self, key: _AnyStr) -> bool: ...
    def __richcmp__(self, other: _Attrib, op: int) -> bool: ...

class QName:
    localname = ...  # type: str
    namespace = ...  # type: str
    text = ...  # type: str
    def __init__(
        self,
        text_or_uri_or_element: Union[None, _AnyStr, _Element],
        tag: Optional[_AnyStr] = ...,
    ) -> None: ...

class _XSLTResultTree(_ElementTree, SupportsBytes):
    def __bytes__(self) -> bytes: ...

class _XSLTQuotedStringParam: ...

# https://lxml.de/parsing.html#the-target-parser-interface
class ParserTarget(Protocol):
    def comment(self, text: _AnyStr) -> None: ...
    def close(self) -> Any: ...
    def data(self, data: _AnyStr) -> None: ...
    def end(self, tag: _AnyStr) -> None: ...
    def start(self, tag: _AnyStr, attrib: Dict[_AnyStr, _AnyStr]) -> None: ...

class ElementClassLookup: ...

class FallbackElementClassLookup(ElementClassLookup):
    fallback: Optional[ElementClassLookup]
    def __init__(self, fallback: Optional[ElementClassLookup] = ...): ...
    def set_fallback(self, lookup: ElementClassLookup) -> None: ...

class CustomElementClassLookup(FallbackElementClassLookup):
    def lookup(
        self, type: str, doc: str, namespace: str, name: str
    ) -> Optional[Type[ElementBase]]: ...

class _BaseParser:
    def copy(self) -> _BaseParser: ...
    def makeelement(
        self,
        _tag: _TagName,
        attrib: Optional[Union[_DictAnyStr, _Attrib]] = ...,
        nsmap: _NSMapArg = ...,
        **_extra: Any,
    ) -> _Element: ...
    def setElementClassLookup(
        self, lookup: Optional[ElementClassLookup] = ...
    ) -> None: ...
    def set_element_class_lookup(
        self, lookup: Optional[ElementClassLookup] = ...
    ) -> None: ...
    @property
    def error_log(self) -> _ErrorLog: ...

class _FeedParser(_BaseParser):
    def close(self) -> _Element: ...
    def feed(self, data: _AnyStr) -> None: ...

class XMLParser(_FeedParser):
    def __init__(
        self,
        encoding: Optional[_AnyStr] = ...,
        attribute_defaults: bool = ...,
        dtd_validation: bool = ...,
        load_dtd: bool = ...,
        no_network: bool = ...,
        ns_clean: bool = ...,
        recover: bool = ...,
        schema: Optional[XMLSchema] = ...,
        huge_tree: bool = ...,
        remove_blank_text: bool = ...,
        resolve_entities: bool = ...,
        remove_comments: bool = ...,
        remove_pis: bool = ...,
        strip_cdata: bool = ...,
        collect_ids: bool = ...,
        target: Optional[ParserTarget] = ...,
        compact: bool = ...,
    ) -> None: ...
    resolvers = ...  # type: _ResolverRegistry

class HTMLParser(_FeedParser):
    def __init__(
        self,
        encoding: Optional[_AnyStr] = ...,
        collect_ids: bool = ...,
        compact: bool = ...,
        huge_tree: bool = ...,
        no_network: bool = ...,
        recover: bool = ...,
        remove_blank_text: bool = ...,
        remove_comments: bool = ...,
        remove_pis: bool = ...,
        schema: Optional[XMLSchema] = ...,
        strip_cdata: bool = ...,
        target: Optional[ParserTarget] = ...,
    ) -> None: ...

class _ResolverRegistry:
    def add(self, resolver: Resolver) -> None: ...
    def remove(self, resolver: Resolver) -> None: ...

class Resolver:
    def resolve(self, system_url: str, public_id: str): ...
    def resolve_file(
        self, f: IO[Any], context: Any, *, base_url: Optional[_AnyStr], close: bool
    ): ...
    def resolve_string(
        self, string: _AnyStr, context: Any, *, base_url: Optional[_AnyStr]
    ): ...

class XMLSchema(_Validator):
    def __init__(
        self,
        etree: _ElementOrTree = ...,
        file: Union[_AnyStr, IO[Any]] = ...,
    ) -> None: ...
    def __call__(self, etree: _ElementOrTree) -> bool: ...

class XSLTAccessControl: ...

class XSLT:
    def __init__(
        self,
        xslt_input: _ElementOrTree,
        extensions: _Dict_Tuple2AnyStr_Any = ...,
        regexp: bool = ...,
        access_control: XSLTAccessControl = ...,
    ) -> None: ...
    def __call__(
        self,
        _input: _ElementOrTree,
        profile_run: bool = ...,
        **kwargs: Union[_AnyStr, _XSLTQuotedStringParam],
    ) -> _XSLTResultTree: ...
    @staticmethod
    def strparam(s: _AnyStr) -> _XSLTQuotedStringParam: ...
    @property
    def error_log(self) -> _ErrorLog: ...

def Comment(text: Optional[_AnyStr] = ...) -> _Comment: ...
def Element(
    _tag: _TagName,
    attrib: Optional[_DictAnyStr] = ...,
    nsmap: _NSMapArg = ...,
    **extra: _AnyStr,
) -> _Element: ...
def SubElement(
    _parent: _Element,
    _tag: _TagName,
    attrib: Optional[_DictAnyStr] = ...,
    nsmap: _NSMapArg = ...,
    **extra: _AnyStr,
) -> _Element: ...
def ElementTree(
    element: _Element = ...,
    file: Union[_AnyStr, IO[Any]] = ...,
    parser: XMLParser = ...,
) -> _ElementTree: ...
def ProcessingInstruction(
    target: _AnyStr, text: _AnyStr = ...
) -> _ProcessingInstruction: ...

PI = ProcessingInstruction

def HTML(
    text: _AnyStr,
    parser: Optional[HTMLParser] = ...,
    base_url: Optional[_AnyStr] = ...,
) -> _Element: ...
def XML(
    text: _AnyStr,
    parser: Optional[XMLParser] = ...,
    base_url: Optional[_AnyStr] = ...,
) -> _Element: ...
def cleanup_namespaces(
    tree_or_element: _ElementOrTree,
    top_nsmap: _NSMapArg = ...,
    keep_ns_prefixes: Optional[Iterable[_AnyStr]] = ...,
) -> None: ...
def parse(
    source: Union[_AnyStr, IO[Any]], parser: XMLParser = ..., base_url: _AnyStr = ...
) -> _ElementTree: ...
def fromstring(
    text: _AnyStr, parser: XMLParser = ..., *, base_url: _AnyStr = ...
) -> _Element: ...
@overload
def tostring(
    element_or_tree: _ElementOrTree,
    encoding: Union[Type[str], Literal["unicode"]],
    method: str = ...,
    xml_declaration: bool = ...,
    pretty_print: bool = ...,
    with_tail: bool = ...,
    standalone: bool = ...,
    doctype: str = ...,
    exclusive: bool = ...,
    with_comments: bool = ...,
    inclusive_ns_prefixes: Any = ...,
) -> str: ...
@overload
def tostring(
    element_or_tree: _ElementOrTree,
    # Should be anything but "unicode", cannot be typed
    encoding: Optional[_KnownEncodings] = ...,
    method: str = ...,
    xml_declaration: bool = ...,
    pretty_print: bool = ...,
    with_tail: bool = ...,
    standalone: bool = ...,
    doctype: str = ...,
    exclusive: bool = ...,
    with_comments: bool = ...,
    inclusive_ns_prefixes: Any = ...,
) -> bytes: ...
@overload
def tostring(
    element_or_tree: _ElementOrTree,
    encoding: Union[str, type] = ...,
    method: str = ...,
    xml_declaration: bool = ...,
    pretty_print: bool = ...,
    with_tail: bool = ...,
    standalone: bool = ...,
    doctype: str = ...,
    exclusive: bool = ...,
    with_comments: bool = ...,
    inclusive_ns_prefixes: Any = ...,
) -> _AnyStr: ...

class Error(Exception): ...

class LxmlError(Error):
    def __init__(
        self, message: Any, error_log: Optional[_BaseErrorLog] = ...
    ) -> None: ...
    error_log: _BaseErrorLog = ...

class DocumentInvalid(LxmlError): ...
class LxmlSyntaxError(LxmlError, SyntaxError): ...

class ParseError(LxmlSyntaxError):
    position: Tuple[int, int]

class XMLSyntaxError(ParseError): ...

class _Validator:
    def assert_(self, etree: _ElementOrTree) -> None: ...
    def assertValid(self, etree: _ElementOrTree) -> None: ...
    def validate(self, etree: _ElementOrTree) -> bool: ...
    @property
    def error_log(self) -> _ErrorLog: ...

class DTD(_Validator):
    def __init__(
        self, file: Union[_AnyStr, IO[Any]] = ..., *, external_id: Any = ...
    ) -> None: ...
    def __call__(self, etree: _ElementOrTree) -> bool: ...

_ElementFactory = Callable[[Any, Dict[_AnyStr, _AnyStr]], _Element]
_CommentFactory = Callable[[_AnyStr], _Comment]
_ProcessingInstructionFactory = Callable[[_AnyStr, _AnyStr], _ProcessingInstruction]

class TreeBuilder:
    def __init__(
        self,
        element_factory: Optional[_ElementFactory] = ...,
        parser: Optional[_BaseParser] = ...,
        comment_factory: Optional[_CommentFactory] = ...,
        pi_factory: Optional[_ProcessingInstructionFactory] = ...,
        insert_comments: bool = ...,
        insert_pis: bool = ...,
    ) -> None: ...
    def close(self) -> _Element: ...
    def comment(self, text: _AnyStr) -> None: ...
    def data(self, data: _AnyStr) -> None: ...
    def end(self, tag: _AnyStr) -> None: ...
    def pi(self, target: _AnyStr, data: Optional[_AnyStr] = ...) -> Any: ...
    def start(self, tag: _AnyStr, attrib: Dict[_AnyStr, _AnyStr]) -> None: ...

def iselement(element: Any) -> TypeGuard[_Element]: ...
